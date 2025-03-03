from django.urls import path
from .views import DefaultSitesListCreateView, DefaultSitesDetailView

app_name="defualtsites"


urlpatterns = [
    path('sites/', DefaultSitesListCreateView.as_view(), name='default-sites-list'),
    path('sites/<int:pk>/', DefaultSitesDetailView.as_view(), name='default-sites-detail'),
]