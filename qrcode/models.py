from django.db import models
from django.utils import timezone

from accounts.models import User
        
    
class QRCode(models.Model):
    created_at = models.DateField(default=timezone.now)
    name = models.CharField(max_length=50)
    qrcode_images = models.FileField(upload_to='qrcode_images/')
    url_or_message = models.CharField(max_length=300, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'qrcode'
        verbose_name_plural = 'QRCode'

    def __str__(self):
        return self.name

    # def create_qrcode(self, url_or_message, name):
    #     import pyqrcode

    #     qrcode = pyqrcode.create(url_or_message)
    #     qrcode.png(f'{name}.png', scale=5)
    #     print(qrcode.terminal())
