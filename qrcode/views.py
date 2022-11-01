from django.shortcuts import redirect, render
from django.core.files import File

import pyqrcode

from .forms import QrcodeCreateForm
from .models import QRCode


def create_qrcode(request):
    create_qrcode_form = QrcodeCreateForm(request.POST or None)
    if create_qrcode_form.is_valid():
        create_qrcode_form.instance.user = request.user
        # create qrcode
        qrcode_name = create_qrcode_form.cleaned_data['name']+'.png'
        created_qrcode = pyqrcode.create(create_qrcode_form.cleaned_data['url_or_message'])
        created_qrcode.png(qrcode_name, scale=10)
        
        destination_file = open(qrcode_name, 'rb')
        create_qrcode_form.instance.qrcode_images.save(qrcode_name, File(destination_file), save=False)
        destination_file.close()
        
        create_qrcode_form.save()
        # get create qrcode
        show_qrcode = QRCode.objects.filter(user=request.user, name=create_qrcode_form.cleaned_data['name']).first()
        print(show_qrcode.qrcode_images.url)
        return render(
            request, 'home.html', context={
                'create_qrcode_form': create_qrcode_form,
                'show_qrcode': show_qrcode
            }
        )
    return render(
        request, 'home.html', context={
            'create_qrcode_form': create_qrcode_form,
        }
    )