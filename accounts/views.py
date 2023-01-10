from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

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
