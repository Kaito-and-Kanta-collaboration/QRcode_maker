from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'is_staff')

    fieldsets = (
        ('ユーザユーザー情報', {'fields': ('username', 'password')}),
        ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        ('ユーザユーザー情報', {'fields': ('username',
         'password', 'confirm_password')}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
