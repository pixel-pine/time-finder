"""
URL configuration for time_finder_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from time_finder_api.views import UserAvailabilityCalendarView, AvailabilityListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/availability/calendar/<str:username>/', UserAvailabilityCalendarView.as_view(), name='user_availability_calendar'),
    path('api/availability/', AvailabilityListCreateView.as_view(), name='availability-list-create'),
]
