from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FormData
from .serializers import FormDataSerializer
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.request import Request
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import generics, mixins

class FormDataListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=FormData.objects.all()
    serializer_class=FormDataSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class FormDataDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = FormData.objects.all()
    serializer_class= FormDataSerializer
    def put(self,request,pk):
        return self.update(request,pk)
    
    def get(self,request,pk):
        return self.retrieve(request)
    
    def delete(self,request,pk):
        return self.destroy(request)