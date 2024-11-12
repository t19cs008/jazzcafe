from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from . import forms

# Create your views here.

class TopView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/top.html'

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'account/login.html'

class LogoutView(LogoutView):
    template_name = 'account/logout.html'

class SignupView(generic.CreateView):
    template_name = 'account/signup.html'
    form_class = forms.SignupForm

    def form_valid(self, form):
        user = form.save()
        return redirect('account:signedup')

class SignedupView(generic.TemplateView):
    template_name = 'account/signedup.html'