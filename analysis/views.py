from django.views.generic import ListView, TemplateView

from . import models

# Create your views here.


# class AnalysisListView(ListView):
#     # model = models.Article 
#     template_name = 'analysis_index.html'

class AnalysisView(TemplateView):
    template_name = 'analysis_index.html'