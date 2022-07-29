from rest_framework import serializers
from .models import Title, Sector, Work_experience, Citezenship, Language, Expert


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'
