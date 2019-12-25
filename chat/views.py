from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse
from .models import Chat
from .forms import ChatForm, PrivateForm


class ChatView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/main.html'


class TopFrame(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/top.html'


class TimeFrame(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/time.html'


class MenuFrame(LoginRequiredMixin, generic.TemplateView):
    template_name = 'chat/menu.html'


class ChatList(LoginRequiredMixin, generic.ListView):
    model = Chat
    template_name = 'chat/message.html'

    def get_queryset(self):
        return self.model.objects.filter(
            Q(room=self.request.room) |
            Q(room__isnull=True)
        )[:int(self.request.user.total_lines)]


class AddMessage(LoginRequiredMixin, generic.CreateView):
    model = Chat
    form_class = ChatForm

    def get_success_url(self):
        return reverse('ctrl')

    def get_form_kwargs(self):
        kwargs = super(AddMessage, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.room = self.request.room
        return super(AddMessage, self).form_valid(form)


class PrivateFrame(AddMessage, generic.CreateView):
    model = Chat
    form_class = PrivateForm
    template_name = 'chat/private.html'

    def get_success_url(self):
        return reverse('private')
