from django.urls import path
from .views import ChatList, TopFrame, TimeFrame, ChatView, AddMessage, MenuFrame


urlpatterns = [
    path('main.html', ChatView.as_view(), name='main'),
    path('window.html', ChatList.as_view(), name='message'),
    path('top.html', TopFrame.as_view(), name='top'),
    path('time.html', TimeFrame.as_view(), name='time'),
    path('ctrl.html', AddMessage.as_view(), name='ctrl'),
    path('menu.html', MenuFrame.as_view(), name='menu'),
    path('private.html', MenuFrame.as_view(), name='private'),
    path('info.html', MenuFrame.as_view(), name='info'),
    path('soobch.html', MenuFrame.as_view(), name='soobch'),
    path('ignore.html', MenuFrame.as_view(), name='ignore'),
    path('nastr.html', MenuFrame.as_view(), name='nastr'),
    path('arch.html', MenuFrame.as_view(), name='arch'),
    path('pravila.html', MenuFrame.as_view(), name='pravila'),
    path('help.html', MenuFrame.as_view(), name='help'),
    path('list_rooms.html', MenuFrame.as_view(), name='list_rooms'),
    path('rooms.html', MenuFrame.as_view(), name='rooms'),
    path('lock.html', MenuFrame.as_view(), name='lock'),
    path('gb.html', MenuFrame.as_view(), name='gb'),
    path('news.html', MenuFrame.as_view(), name='news'),
    path('vstrechi.html', MenuFrame.as_view(), name='vstrechi'),
    path('games.html', MenuFrame.as_view(), name='games'),
]
