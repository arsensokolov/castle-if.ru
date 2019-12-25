from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Chat
from .forms import ChatForm


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
        return self.model.objects.filter(room=self.request.room)[:int(self.request.user.total_lines)]


class AddMessage(LoginRequiredMixin, generic.CreateView):
    model = Chat
    # fields = ['message']
    success_url = '/ctrl.html'
    form_class = ChatForm

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
