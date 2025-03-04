from rest_framework import generics
from .models import DefaultSites
from .serializers import DefaultSitesSerializer

# List and Create API View
class DefaultSitesListCreateView(generics.ListCreateAPIView):
    queryset = DefaultSites.objects.all()
    serializer_class = DefaultSitesSerializer

# Retrieve, Update, and Delete API View
class DefaultSitesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DefaultSites.objects.all()
    serializer_class = DefaultSitesSerializer
