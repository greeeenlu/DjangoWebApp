from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calculator, name='home'),
    path('calculator/<str:newResult>/<str:lastResult>/<str:lastOperator>/<int:reset>/', views.calculator),
    path('calculator/digit/<str:digit>/<str:previous>/<str:lastResult>/<str:lastOperator>/<int:reset>/', views.digitInput, name= 'digitInput'),
    path('calculator/operator/<str:operator>/<str:newResult>/<str:lastResult>/<str:lastOperator>/<int:reset>/', views.operatorInput, name= 'operatorInput'),
]