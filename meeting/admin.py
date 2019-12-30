from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Album, Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'album']
    list_display_links = ['title', 'id',]
    list_filter = ['album',]
    readonly_fields = ['preview',]
    search_fields = ['title',]
