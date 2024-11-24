from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.todo_list, name='todo_list'),
#     path('create', views.todo_create, name='todo_create'),
#     path('<int:pk>/update/', views.todo_update, name='todo_update'),
#     path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),
# ]

urlpatterns = [
    path('', views.renters_list, name='renters_list'),
    path('create', views.renters_create, name='renters_create'),
    path('<uuid:pk>/update/', views.renters_update, name='renters_update'),
    path('<uuid:pk>/delete/', views.renters_delete, name='renters_delete'),
]
