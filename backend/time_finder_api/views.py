from django.shortcuts import render
from rest_framework import generics, permissions
from . import serializers,models

# Create your views here.

class Calendar(generics.ListCreateAPIView):
    queryset = models.Availability.objects.all()
    serializer_class = serializers.AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
