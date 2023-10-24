from django.urls import path
from . import views

urlpatterns = [
    path('', views.contas, name='contas'),
    path('cliente/<str:pk>', views.clientPage, name='cliente')
]
