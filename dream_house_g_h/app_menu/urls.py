from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('list_staff', views.list_staff, name='list_staff'),
    path('list_branch', views.list_branch, name='list_branch'),
    path('list_clients', views.list_clients, name='list_clients'),
    path('hire_staff', views.hire_staff, name='hire_staff'),
    path('update_staff', views.update_staff, name='update_staff'),
    path('register_client',views.register_client, name ='register_client'),
    path('update_client', views.update_client, name='update_client'),
    path('find_branch', views.find_branch, name='find_branch'),
    path('update_branch', views.update_branch, name='update_branch'),
    path('open_branch', views.open_branch, name='open_branch'),

]
