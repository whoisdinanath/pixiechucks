from speech_main.src import main_func
from rest_framework import generics
from django.shortcuts import redirect
from rest_framework.views import APIView
from .models import Input
from .serializers import InputSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


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
                snippets = Input.objects.last()
                file = snippets.audio_file
                text = snippets.text
                resp = main_func(text, file)
                return Response(resp)
            return Response(serializer.errors, status=400)


# class Endpoint(generics.GenericAPIView):
#     # override post request
#     def post(self, request, *args, **kwargs):
#         # get the file from the request
#         if request.method == 'POST':
#             file = request.FILES['audio_file']
#             text = request.POST['text']
#             data = main_func(text, file)
#             return Response(data)
#     # override get request

#     def get(self, request, *args, **kwargs):
#         return Response("API is working", status=200)


# class OutputList(APIView):
#     # permission_classes = [IsAuthenticated]
#     def get(self, request):
#         if request.method == 'GET':
#             snippets = Input.objects.last()
#             file = snippets.audio_file
#             text = snippets.text
#             data = main_func(text, file)
#             snippets.delete()
#             return Response(data)
