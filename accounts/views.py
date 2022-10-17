from django.shortcuts import redirect, render
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm


class UserLoginView(FormView):
    template_name = 'accounts/accounts_login.html'
    form_class = UserLoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('qrcode:home')
        else:
            form = UserLoginForm()
            return render(request, 'accounts/accounts_login.html', {'form': form})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('qrcode:home')
        else:
            return redirect('accounts:login')


    