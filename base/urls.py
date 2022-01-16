from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_register, name='login'),
    path('register/', views.registeruser, name='register'),
    path('logout/', views.logoutuser, name='logout'),
    path('room/<str:pk>', views.room, name='room'),
    path('profile/<str:pk>', views.userprofile, name='userprofile'),
    path('updateuser/<str:pk>', views.updateuser, name='updateuser'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>', views.deletemessage, name='delete-message'),
    path('topics/', views.topicspage, name='topics'),
    path('activity/', views.activitypage, name='activity'),
]
