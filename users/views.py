from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
