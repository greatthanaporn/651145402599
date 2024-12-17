from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.c_list, name='c_list'),
    path('ser_id/', views.ser_id, name='ser_id'),
    path('ser_name/', views.ser_name, name='ser_name'),
    path('edit/<str:c_id>/', views.edit, name='edit'),
    path('delete', views.delete, name='delete')

]