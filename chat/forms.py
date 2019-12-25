from django import forms
from djantimat.helpers import PymorphyProc
from .models import Chat


class ChatForm(forms.ModelForm):
    message = forms.CharField(min_length=1, max_length=400, widget=forms.TextInput(attrs={'size': 37}))

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
            raise forms.ValidationError('вы уже отправляли такое сообщение', code='invalid')
        return message
