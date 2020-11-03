from django.urls import path

from .views import api, home

urlpatterns = [
    path("", home),
    path("api", api)
]
