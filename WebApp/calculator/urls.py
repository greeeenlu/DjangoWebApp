from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calculator, name='index'),
    path('calculator/', views.calculator)
]
