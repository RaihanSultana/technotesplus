from django.urls import path
from django.views.generic import TemplateView

from .views import UserRegistrationView, login_view

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', login_view, name='login'),
]
