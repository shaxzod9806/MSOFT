from rest_framework import serializers
from .models import Title, Sector, Work_experience, Citezenship, Language, Expert


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


class Work_experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_experience
        fields = '__all__'


class CitezenshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citezenship
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
