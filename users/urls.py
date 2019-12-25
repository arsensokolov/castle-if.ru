from django.urls import path, reverse
from .views import LoginPage, LogoutPage, RegisterPage, OnlineUsers


urlpatterns = [
    path('', LoginPage.as_view(), name='login'),
    path('exit.html', LogoutPage.as_view(), name='logout'),
    path('reg.html', RegisterPage.as_view(), name='register'),
    path('users.html', OnlineUsers.as_view(), name='users'),
]
