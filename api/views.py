from speech_main.src import main_func
from rest_framework import generics
from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import Input
from .serializers import InputSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HomeView(APIView):
    def get(self, request):
        return Response("API is working", status=200)


class InputCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Input.objects.all()
    serializer_class = InputSerializer

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = InputSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('output')
            return Response(serializer.errors, status=400)


class Endpoint(generics.GenericAPIView):
    pass


class OutputList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.method == 'GET':
            snippets = Input.objects.last()
            file = snippets.audio_file
            text = snippets.text
            data = main_func(text, file)
            snippets.delete()
            return Response(data)
