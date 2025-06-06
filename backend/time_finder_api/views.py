from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from .serializers import AvailabilitySerializer
from .models import Availability

# Create your views here.

class UserAvailabilityCalendarView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #May want to remove ReadOnly later

    def get(self, request, username):
        user = get_object_or_404(User, username=username)

        # Get current week:
        today = timezone.now()
        start_of_week = today - timezone.timedelta(days=today.weekday())
        end_of_week = start_of_week + timezone.timedelta(days = 6, hours = 23, minutes = 59, seconds = 59) #includes all times on last day of the week

        # Get user's availability slots for current week:
        availability_slots = Availability.objects.filter(
            user=user,
            start_time__range=(start_of_week, end_of_week) #using __range lookup for start_time field
        ).order_by('start_time')

        calendar_data = [] #list that holds the data of all time slots
        for slot in availability_slots:
            calendar_data.append({
                'start': slot.start_time.isoformat(), # start_time of each instance of slot, isoformat formats the time
                'end': slot.end_time.isoformat(),
                'title' : 'Available',
            })

        return Response(calendar_data) #indent outside of look so it returns all slots

class AvailabilityListCreateView(generics.ListCreateAPIView):
    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #Gets availability slots for the user currently logged in
        return Availability.objects.filter(user=self.request.user)

    def perform_create(self, serializer): #called when a POST request is made to create new instance of a model
        #automatically assigns the logged in user to the new instance of Availability model
        serializer.save(user=self.request.user) #serializer validates data and creates a new instance of the model, save method saves the new model to the database
