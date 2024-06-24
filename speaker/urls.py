from speaker.views import speaker
from django.contrib import admin
from django.urls import path
from .views import speakers, speaker

urlpatterns = [
    # path("", speakers),
    path("<str:key>/", speaker),
]
