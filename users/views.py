from django.views.generic import DetailView,TemplateView,CreateView
from .models import CustomUser
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.


class UsersPage(TemplateView):

    template_name = 'home.html'
    



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"