from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView


from .forms import CreateQRCodeForm


def create_and_show_qrcode_view(request):
    qrcode_form = CreateQRCodeForm(request.POST or None)
    if qrcode_form.is_valid():
        qrcode_form.instance.user = request.user
        qrcode_form.save()
        return redirect('qrcode:home')
    return render(request, 'home.html', context={'create_qrcode_form': qrcode_form})
    
    