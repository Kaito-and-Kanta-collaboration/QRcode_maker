from django.urls import path


from . import views


app_name = 'qrcode'

urlpatterns = [
    path('', views.create_qrcode, name='home'),
    path('<slug:username>/qrcode_list', views.UserQrcodeList.as_view(), name='user_qrcode_list'),
    path('qrocde_detail/<int:pk>', views.UserQrcodeDetail.as_view(), name='qrcode_detail'),
]
