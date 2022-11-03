import os

from django.shortcuts import redirect, render
from django.core.files import File

from .forms import QrcodeCreateForm
from .models import QRCode


def create_qrcode(request):
    create_qrcode_form = QrcodeCreateForm(request.POST or None)
    if create_qrcode_form.is_valid():
        create_qrcode_form.instance.user = request.user
        
        qrcode_name = create_qrcode_form.cleaned_data['name']
        url_or_message = create_qrcode_form.cleaned_data['url_or_message']
        qrcode_name = create_qrcode_form.create_qrcode(url_or_message, qrcode_name)

        with open(qrcode_name, 'rb') as destination_file:
            create_qrcode_form.instance.qrcode_images.save(qrcode_name, File(destination_file), save=False)

        os.remove(qrcode_name) # Delete created image on base directory
        
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