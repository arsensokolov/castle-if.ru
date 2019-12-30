from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import Room, Chat, Smile


@admin.register(Room)
class RoomAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_private']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['room', 'created_at', 'user', 'message', 'message_type']
    search_fields = ['message']
    list_filter = ['room', 'user', 'created_at']


@admin.register(Smile)
class SmileAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['code', 'smile_preview']
    search_fields = ['code']
    readonly_fields = ['smile_preview']
