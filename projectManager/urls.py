from django.contrib import admin
from django.urls import path
from engine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.users, name='users'),
    path('adduser/', views.adduser, name='adduser'),
    path('registeruser', views.registeruser, name='registeruser'),
    path('setPassword/<str:sessionID>/', views.setPassword, name='setPassword'),
    path('viewProfile/<int:id>', views.viewProfile, name='viewProfile'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
    path('updateUser/<int:id>', views.updateUser, name='updateUser'),
    path('projectsList/', views.projectsList, name='projectsList'),
    path('clientsList/', views.clientsList, name='clientsList'),
    path('addclient/', views.addclient, name='addclient'),
    path('registerclient', views.registerclient, name='registerclient'),
    path('viewClient/<int:id>', views.viewClient, name='viewClients'),
    path('updateClient/<int:id>', views.updateClient, name='updateClient'),
    path('deleteClient/<int:id>', views.deleteClient, name='deleteClient'),
]