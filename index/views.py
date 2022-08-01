from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Expert, Title, Sector, Work_experience, Citezenship, Language
from .serializers import ExpertSerializer, TitleSerializer, SectorSerializer, Work_experienceSerializer, \
    CitezenshipSerializer, LanguageSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ExpertAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    token = openapi.Parameter('Authorization', in_=openapi.IN_HEADER, type=openapi.TYPE_STRING, description='Token')

    @swagger_auto_schema(request_body=ExpertSerializer, manual_parameters=[token], parser_classes=parser_classes)
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token == "n4j6lnZ^D%w5*@APV%7Q%FxQM":
            serializer = ExpertSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class TitleAPI(APIView):
    def get(self, request):
        title = Title.objects.all()
        serializer = TitleSerializer(title, many=True)
        return Response(serializer.data)


class SectorApi(APIView):
    def get(self, request):
        sector = Sector.objects.all()
        serializer = SectorSerializer(sector, many=True)
        return Response(serializer.data)


class Work_experienceApi(APIView):
    def get(self, request):
        work_experience = Work_experience.objects.all()
        serializer = Work_experienceSerializer(work_experience, many=True)
        return Response(serializer.data)


class CitezenshipApi(APIView):
    def get(self, request):
        citezenship = Citezenship.objects.all()
        serializer = CitezenshipSerializer(citezenship, many=True)
        return Response(serializer.data)


class LanguageApi(APIView):
    def get(self, request):
        language = Language.objects.all()
        serializer = LanguageSerializer(language, many=True)
        return Response(serializer.data)
