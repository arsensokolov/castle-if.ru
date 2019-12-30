from django.urls import path
from . import views


urlpatterns = [
    path('', views.AlbumList.as_view(), name='vstrechi'),
    path('<year>/<month>/<day>/', views.PhotoList.as_view(), name='photos'),
    path('photo/<pk>/', views.PhotoDetail.as_view(), name='photo'),
]