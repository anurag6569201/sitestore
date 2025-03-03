from rest_framework import serializers
import sites.models as models


class SiteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.Site
        fields = '__all__'