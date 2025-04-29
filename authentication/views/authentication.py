from django.contrib.auth import login, logout
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.views import View

from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from authentication.forms import UserRegistrationForm, UserLoginForm
from authentication.models import User


class UserCreateView(UserPassesTestMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'authentication/register.html'
    extra_context = {'title': 'Vortex | Регистрация', 'form': UserRegistrationForm}

    def test_func(self):
        return self.request.user.is_anonymous

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('index')


class UserLoginView(UserPassesTestMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'authentication/login.html'
    extra_context = {'title': 'Vortex | Вход'}

    def test_func(self):
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('index')


class ShowProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'authentication/profile.html'
    extra_context = {'title': 'Vortex | Профиль'}
    context_object_name = 'page_user'

    def get_object(self):
        return self.request.user


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')