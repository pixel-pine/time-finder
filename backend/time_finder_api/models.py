from django.db import models
from django.contrib.auth.models import User
# We are using django auth as a system for allowing each user to log in

# Create your models here.

# Here users can specify time blocks where they are available
class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_recurring = models.BooleanField(default=False)
    recurring_end = models.DateTimeField(null=True, blank=True) #time/date when recurring event will end

    class Meta:
        unique_together = ('user', 'start_time', 'end_time')
        verbose_name = "Availability"
        verbose_name_plural = "Availabilities" #Stating plural name because django adds an s to make a name plural

