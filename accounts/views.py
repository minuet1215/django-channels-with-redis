from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name='partials/form.html',
    extra_context={
        "form_name": "Sign-up",
        "submit_lable": "Sign-up"
    },
    success_url=reverse_lazy("accounts:login")
)

login = LoginView.as_view(
    template_name='partials/form.html',
    extra_context={
        'form_name': "login",
        'submit_label': 'login',
    }
)

logout = LogoutView.as_view(
    next_page='accounts:login',
)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


profile = ProfileView.as_view()
