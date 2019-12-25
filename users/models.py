from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from colorfield.fields import ColorField


class User(AbstractUser):
    REFRESH_TIME = (
        (10, 10),
        (12, 12),
        (14, 14),
        (18, 18),
        (20, 20),
        (25, 25),
        (30, 30),
        (50, 50),
    )
    TOTAL_LINES = (
        (10, 10),
        (15, 15),
        (20, 20),
        (25, 25),
        (30, 30),
        (35, 35),
    )
    nik_color = ColorField('цвет ника', default='#ff0000')
    msg_color = ColorField('цвет сообщения', default='#ff0000')
    refresh_time = models.PositiveSmallIntegerField('время обноелния', default=14, choices=REFRESH_TIME)
    total_lines = models.PositiveSmallIntegerField('число строк', default=25, choices=TOTAL_LINES)
    show_smiles = models.BooleanField('показ смайлов', default=True)
    js_on = models.BooleanField('вкл. Java-script', default=True)
    show_avatar = models.BooleanField('показ аватар', default=False, help_text='картинка вместо ника')
    icq_uin = models.PositiveIntegerField('ICQ UIN', null=True, blank=True)
    about = models.TextField('немного о себе', null=True, blank=True)

    last_activity = models.DateTimeField(default=timezone.now, editable=False)
    is_offline = models.BooleanField(default=True, editable=False)

    @property
    def is_online(self):
        return not self.is_sleep and not self.is_offline

    @property
    def is_sleep(self):
        return self.last_activity + timedelta(minutes=15) < timezone.now()
