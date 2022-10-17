from email.policy import default
from django.db import models
from django.utils import timezone

from accounts.models import User

# Create your models here.
class QRCode(models.Model):
    created_at = models.DateField(default=timezone.now)
    name = models.CharField(max_length=50)
    qrcode_images = models.FileField(upload_to='qrcode_image/')
    url_or_message = models.CharField(max_length=150, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'qrcode'
        verbose_name_plural = 'QRCode'