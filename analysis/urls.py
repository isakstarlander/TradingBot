from django.urls import path

from . import views

urlpatterns = [
    # path('', views.AnalysisListView.as_view(), name='analysis'),
    path('', views.AnalysisView.as_view(), name='analysis'),
]