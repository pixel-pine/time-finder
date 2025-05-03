from rest_framework import serializers

from . import models


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Availability
        fields = "__all__"
        read_only_fields = ['user'] # To prevent users from setting user field manually