from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.edit import FormView


from .forms import CreateQRCodeForm


def create_and_show_qrcode_view(request):
    create_qrcode_form = CreateQRCodeForm(request.POST or None)
    if create_qrcode_form.is_valid():
        create_qrcode_form.instance.user = request.user
        create_qrcode_form.save()
    return render(request, 'home.html', context={'create_qrcode_form': create_qrcode_form})
    
    