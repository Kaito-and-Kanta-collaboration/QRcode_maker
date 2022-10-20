from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserCreationForm


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


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


class UserSignupView(FormView):
    template_name = 'accounts/accounts_signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('qrcode:home')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('qrcode:home')
        else:
            form = UserCreationForm()
            return render(request, 'accounts/accounts_signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('qrcode:home')
            else:
                return render(request, 'accounts/accounts_signup.html', {'form': form})
