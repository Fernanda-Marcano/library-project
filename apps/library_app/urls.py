from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.autor_create)
]
