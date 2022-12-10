import os

from django.shortcuts import render
from django.core.files import File
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404  
from django.http import JsonResponse

from accounts.models import User

from .forms import QrcodeCreateForm
from .models import QRCode


@login_required
def create_qrcode(request):
    create_qrcode_form = QrcodeCreateForm(request.POST or None)
    if create_qrcode_form.is_valid():
        create_qrcode_form.instance.user = request.user
        
        qrcode_name = create_qrcode_form.cleaned_data['name']
        url_or_message = create_qrcode_form.cleaned_data['url_or_message']
        qrcode_name = create_qrcode_form.create_qrcode(url_or_message, qrcode_name)

        with open(qrcode_name, 'rb') as destination_file:
            create_qrcode_form.instance.qrcode_images.save(qrcode_name, File(destination_file), save=False)

        # Delete created image on base directory
        os.remove(qrcode_name) 
        
        create_qrcode_form.save()

        # Get created image to display it
        show_qrcode = QRCode.objects.get(name=create_qrcode_form.cleaned_data['name'])

        return render(
            request, 'home.html', context={
                'create_qrcode_form': create_qrcode_form,
                'show_qrcode': show_qrcode
            }
        )

    return render(
        request, 'home.html',{ 'create_qrcode_form': create_qrcode_form,}
    )
    

class CheckForUserMatchMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        target_qrcode = get_object_or_404(QRCode, pk=self.kwargs['pk'])
        return self.request.user == target_qrcode.user
        
    def handle_no_permission(self):
        return JsonResponse(
            {'message': 'Only user who made this qrcode have access to this view'}
        )


class UserQrcodeList(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'qrcode/user_qrcode_list.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qrcode_list'] = QRCode.objects.filter(user=self.object).all()
        if self.request.user == self.object:
            context['have_the_right_of_access'] = True
        else:
            context['have_the_right_of_access'] = False
        return context
    
    
class UserQrcodeDetail(CheckForUserMatchMixin, DetailView):
    model = QRCode
    template_name = 'qrcode/qrcode_detail.html'
    