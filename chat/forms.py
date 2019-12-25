from django import forms
from django.contrib.auth import get_user_model
from djantimat.helpers import PymorphyProc
from .models import Chat

User = get_user_model()

ERROR_FLOOD_MESSAGE = 'вы уже отправляли такое сообщение'


class ChatForm(forms.ModelForm):
    message = forms.CharField(max_length=400, widget=forms.TextInput(attrs={'size': 37}))

    class Meta:
        model = Chat
        fields = ['message']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ChatForm, self).__init__(*args, **kwargs)

    def clean_message(self):
        message = self.cleaned_data['message']
        message = PymorphyProc.replace(message, repl='@@@')
        last_messages = Chat.objects.filter(user=self.user).values_list('message', flat=True)[:5]

        if message in last_messages:
            raise forms.ValidationError(ERROR_FLOOD_MESSAGE, code='invalid')
        return message


class PrivateForm(ChatForm):
    message = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'size': 15}))

    class Meta:
        model = Chat
        fields = ['to', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs.pop('user')
        self.fields['to'].queryset = User.objects.exclude(id=self.user.id)

    def clean_message(self):
        message = self.cleaned_data['message']
        to_user = self.cleaned_data['to']
        message = PymorphyProc.replace(message, repl='@@@')
        last_messages = Chat.objects.filter(
            user=self.user,
            to=to_user
        ).values_list('message', flat=True)[:5]

        if message in last_messages:
            raise forms.ValidationError(ERROR_FLOOD_MESSAGE, code='invalid')
        return message
