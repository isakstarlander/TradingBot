from django.urls import path 

from django.contrib.auth import views as auth_views
from .forms import CustomAuthForm

from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.login, name='login', kwargs={"authentication_form":CustomAuthForm}),
]