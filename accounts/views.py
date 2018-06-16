from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login, logout as django_logout
from django.views import View

from accounts.forms import SignUpForm
from accounts.forms import LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            form = SignUpForm()
            messages.success(request, 'Thank you for joining!!')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form, 'title':"Signup Form",'claim': "Please enter your details to register a new user"})

class LoginView(View):

    def get(self, request):
        """
        Muestra el formulario de login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm()
        context = {'form': form}
        context['title'] = 'User Login'
        context['claim'] = 'Please login with your account'
        return render(request, 'accounts/login.html', context)

    def post(self, request):
        """
        Procesa el login de un usuario
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # comprobamos si las credenciales son correctas
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Wrong username or password')
            else:
                # iniciamos la sesión del usuario (hacemos login del usuario)
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        context = {'form': form}
        context['title'] = 'Login'
        context['claim'] = 'Thank you for logging in'
        return render(request, 'accounts/login.html', context)


class LogoutView(View):

    def get(self, request):
        """
        Hace logout de un usuario y le redirige al login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse de redirección al login
        """
        django_logout(request)
        return redirect('acc-login')