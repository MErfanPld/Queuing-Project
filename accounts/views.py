from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth import login
from django.conf import settings
from .forms import UserLoginForm
from django.contrib.auth import login, get_backends

from users.models import User


class UserLoginView(FormView):
    template_name = 'auth/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.cleaned_data['user']
        if not hasattr(user, 'backend'):
            user.backend = get_backends()[0].__class__.__module__ + "." + get_backends()[0].__class__.__name__
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
