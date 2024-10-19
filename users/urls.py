from django.urls import path
from .views import UsersPage,SignUpView

urlpatterns = [
    path('',UsersPage.as_view(),name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
]