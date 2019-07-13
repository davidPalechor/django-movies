from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy


class UserSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('user:login')
    template_name = 'signup.html'


class UserLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)