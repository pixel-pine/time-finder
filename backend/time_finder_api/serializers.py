from rest_framework import serializers

from . import models


class AvailabilitySerializerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Availability
        fields = "__all__"