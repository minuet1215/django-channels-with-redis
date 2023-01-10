from django.contrib.auth.views import LogoutView, LoginView

# Create your views here.
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
