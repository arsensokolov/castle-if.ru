from django.db import models
from django.utils.safestring import mark_safe


def photo_upload(instance, filename):
    day = '{}/{}/{}'.format(
        instance.album.date.year,
        instance.album.date.month,
        instance.album.date.day,
    )
    return 'meeting/{0}/{1}'.format(day, filename)


class Album(models.Model):
    title = models.CharField('заголовок', max_length=60)
    date = models.DateField('дата встречи')

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'
        ordering = ['-date']

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.PROTECT, verbose_name='альбом', related_name='photos')
    title = models.CharField('подпись к фото', max_length=140, null=True, blank=True)
    image = models.ImageField('фото', upload_to=photo_upload)
    my_order = models.PositiveIntegerField('сортировка', default=0)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'
        ordering = ['my_order']

    def __str__(self):
        return '({}) {}'.format(self.id, self.title)

    def preview(self):
        return mark_safe('<img src="{}">'.format(self.image.url))
    preview.short_description = 'просмотр'