from django.urls import path, include
from .import views

urlpatterns = [
    path('heart_disease/',views.heart_disease,name='heart_disease'),
]