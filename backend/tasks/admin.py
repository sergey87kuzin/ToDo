from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'header', 'author')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Task, TaskAdmin)
admin.site.unregister(Group)
