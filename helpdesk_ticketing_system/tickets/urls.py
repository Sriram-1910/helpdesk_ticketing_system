from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('new/', views.ticket_create, name='ticket_create'),
]
