from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from .forms import QrcodeCreateForm
from .models import QRCode


# class QrcodeCreateView(CreateView):
#     template_name = 'home.html'
#     form_class = QrcodeCreateForm

#     def get(self, request):
#         qrcode_form = QrcodeCreateForm()
#         return render(request, 'home.html', context={'create_qrcode_form': qrcode_form})

#     def post(self, request):
#         qrcode_form = QrcodeCreateForm(request.POST)
#         if qrcode_form.is_valid():
#             url_or_message = qrcode_form.cleaned_data['url_or_message']
#             name = qrcode_form.cleaned_data['name']
#             QRCode.create_qrcode(self, url_or_message=url_or_message, name=name)
#             return render(request, 'home.html', context={'create_qrcode_form': qrcode_form})
#         return redirect('qrcode:home')

def create_qrcode(request):
    create_qrcode_form = QrcodeCreateForm(request.POST or None)
    if create_qrcode_form.is_valid():
        create_qrcode_form.instance.user = request.user
        create_qrcode_form.save()
        return redirect('qrcode:home')
    return render(
        request, 'home.html', context={
            'create_qrcode_form': create_qrcode_form
        }
    )