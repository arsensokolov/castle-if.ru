from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import User

COLORS = (
    ('#CFCFCF', 'Светло-серый'),
    ('#00FFFF', 'Бирюзовый'),
    ('#0000FF', 'Синий'),
    ('#A52A2A', 'Коричневый'),
    ('#006400', 'Темно-зеленый'),
    ('#90EE90', 'Светло-зеленый'),
    ('#808080', 'Серый'),
    ('#008000', 'Зеленый'),
    ('#FFA500', 'Оранжевый'),
    ('#FFC0CB', 'Розовый'),
    ('#FF0000', 'Красный'),
    ('#EE82EE', 'Фиолетовый'),
    ('#FFFFFF', 'Белый'),
    ('#FFFF00', 'Желтый'),
    ('#800000', 'Спелая вишня'),
    ('#000080', 'Морской'),
    ('#FF00FF', 'Сиреневый'),
    ('#ADD8E6', 'Светло-синий'),
    ('#F4A460', 'Песочный'),
    ('#A0522D', 'Древесный'),
    ('#7FFFD4', 'Аквамарин'),
)


class RegisterForm(UserCreationForm):
    nik_color = forms.ChoiceField(
        label='цвет ника',
        widget=forms.Select(),
        choices=COLORS,
        initial='#FF0000'
    )
    msg_color = forms.ChoiceField(
        label='цвет сообщений',
        widget=forms.Select(),
        choices=COLORS,
        initial='#FF0000'
    )
    about = forms.ChoiceField(
        label='немного о себе',
        widget=forms.Textarea(attrs={'cols': 39, 'rows': 8}),
        required=False
    )

    class Meta:
        model = User
        fields = (
            'username',
            'nik_color',
            'msg_color',
            'refresh_time',
            'total_lines',
            'show_smiles',
            'js_on',
            'show_avatar',
            'email',
            'icq_uin',
            'about'
        )
