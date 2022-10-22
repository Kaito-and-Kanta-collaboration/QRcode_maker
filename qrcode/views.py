from django.shortcuts import redirect, render
from django.views.generic.edit import FormView

from .forms import QrcodeCreateForm


class QrcodeCreateView(FormView):
    template_name = 'home.html'
    form_class = QrcodeCreateForm

    def get(self, request):
        qrcode_form = QrcodeCreateForm()
        return render(request, 'home.html', context={'create_qrcode_form': qrcode_form})
    
    # def post(self, request):