from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('list_staff', views.list_staff, name='list_staff'),
    path('list_branch', views.list_branch, name='list_branch'),
    path('list_clients', views.list_clients, name='list_clients'),
    path('hire_staff', views.hire_staff, name='hire_staff'),
    path('update_staff', views.update_staff, name='update_staff'),
    path('register_client',views.register_client, name ='register_client')
]
