from django.urls import path


from . import views


app_name = 'qrcode'

urlpatterns = [
    path('', views.QrcodeCreateView.as_view(), name='home'),
]
