from django.urls import path
from . import views

urlpatterns = [
    path('', views.feriado_index),
]


