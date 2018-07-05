from django.views.generic import ListView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

# Create your views here.


# class AnalysisListView(ListView):
#     # model = models.Article 
#     template_name = 'analysis_index.html'

class AnalysisView(LoginRequiredMixin, TemplateView):
    template_name = 'analysis_index.html'
    login_url = 'login'