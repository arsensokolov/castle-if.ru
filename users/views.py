from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from chat.models import Chat
from .models import User
from .forms import RegisterForm


class LoginPage(LoginView):
    redirect_authenticated_user = True

    def form_valid(self, form):
        login(self.request, form.get_user())
        if self.request.user.is_authenticated:
            self.request.user.is_offline = False
            self.request.user.save()
            Chat.objects.create(user=self.request.user, message_type=Chat.USER_LOGIN)
        return HttpResponseRedirect(self.get_success_url())


class LogoutPage(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        self.request.user.is_offline = True
        self.request.user.save()
        Chat.objects.create(user=self.request.user, message_type=Chat.USER_LOGOUT)
        return super(LogoutPage, self).dispatch(request, *args, **kwargs)


class RegisterPage(generic.CreateView):
    model = User
    form_class = RegisterForm
    success_url = '/main.html'


class OnlineUsers(generic.ListView):
    model = User

    def get_queryset(self):
        queryset = self.model.objects.exclude(is_offline=True).order_by('-last_activity')
        return queryset
