from django.urls import path

from gps import views


urlpatterns = [
    path('gps/', views.consular_gps),
]
