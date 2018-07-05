from django.views.generic import ListView, TemplateView

from . import models

# Create your views here.


# class PortfolioListView(ListView):
#     # model = models.Article 
#     template_name = 'portfolio_index.html'

class PortfolioView(TemplateView):
    template_name = 'portfolio_index.html'