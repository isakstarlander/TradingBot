from django.views.generic import ListView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

# Create your views here.


# class PortfolioListView(ListView):
#     # model = models.Article 
#     template_name = 'portfolio_index.html'

class PortfolioView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio_index.html'
    login_url = 'login'