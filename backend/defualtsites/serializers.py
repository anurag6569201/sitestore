from rest_framework import serializers
from .models import DefaultSites

class DefaultSitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultSites
        fields = '__all__'  # Serialize all fields
