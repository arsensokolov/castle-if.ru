from django.db import models
from django.conf import settings
from django.utils import timezone


class Room(models.Model):
    name = models.CharField('название камеры', max_length=60)
    slug = models.SlugField('код камеры')
    is_private = models.BooleanField('приватная', default=True)
    my_order = models.PositiveIntegerField('сортировка', default=0, blank=False, null=True)

    class Meta:
        ordering = ['my_order']
        verbose_name = 'комната'
        verbose_name_plural = 'комнаты'

    def __str__(self):
        return self.name


class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='отправитель')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='комната')
    message = models.TextField('сообщение')
    to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='получатель',
        blank=True,
        null=True,
        related_name='+'
    )
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'чат'
        verbose_name_plural = 'чаты'

    def __str__(self):
        return '[{}] {}: {}'.format(self.created_at, self.user.username, self.message)
