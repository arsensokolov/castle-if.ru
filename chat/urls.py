from django.urls import path
from . import views


urlpatterns = [
    path('main.html', views.ChatView.as_view(), name='main'),
    path('window.html', views.ChatList.as_view(), name='message'),
    path('top.html', views.TopFrame.as_view(), name='top'),
    path('time.html', views.TimeFrame.as_view(), name='time'),
    path('ctrl.html', views.AddMessage.as_view(), name='ctrl'),
    path('menu.html', views.MenuFrame.as_view(), name='menu'),
    path('private.html', views.PrivateFrame.as_view(), name='private'),
    path('info.html', views.MenuFrame.as_view(), name='info'),
    path('soobch.html', views.MenuFrame.as_view(), name='soobch'),
    path('ignore.html', views.MenuFrame.as_view(), name='ignore'),
    path('nastr.html', views.MenuFrame.as_view(), name='nastr'),
    path('arch.html', views.MenuFrame.as_view(), name='arch'),
    path('pravila.html', views.PravilaView.as_view(), name='pravila'),
    path('help/index.html', views.HelpPages.as_view(), name='help'),
    path('help/<page>.html', views.HelpPages.as_view(), name='help'),
    path('list_rooms.html', views.MenuFrame.as_view(), name='list_rooms'),
    path('rooms.html', views.MenuFrame.as_view(), name='rooms'),
    path('lock.html', views.MenuFrame.as_view(), name='lock'),
    path('gb.html', views.MenuFrame.as_view(), name='gb'),
    path('news.html', views.MenuFrame.as_view(), name='news'),
    path('vstrechi.html', views.MenuFrame.as_view(), name='vstrechi'),
    path('games.html', views.MenuFrame.as_view(), name='games'),
]
