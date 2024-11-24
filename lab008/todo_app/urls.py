from django.urls import path
from . import views


urlpatterns = [
    path('', views.renters_list, name='renters_list'),
    path('create', views.renters_create, name='renters_create'),
    path('<uuid:pk>/update/', views.renters_update, name='renters_update'),
    path('<uuid:pk>/delete/', views.renters_delete, name='renters_delete'),
]
