from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from .serializers import ExpertSerializer
from drf_yasg.utils import swagger_auto_schema


class ExpertAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(request_body=ExpertSerializer, parser_classes=parser_classes)
    def post(self, request):
        serializer = ExpertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
