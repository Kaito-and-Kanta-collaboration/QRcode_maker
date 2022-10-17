from django.urls import path


from . import views


app_name = 'qrcode'

urlpatterns = [
    path('', views.create_and_show_qrcode_view, name='create_and_show_qrcode'),
]
