from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calculator),
    path('calculator/<str:result>', views.calculator),
    path('calculator/digit/<str:digit>/<str:previous>', views.digitInput, name= 'digitInput')
]