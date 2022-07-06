
from django.contrib import admin

# Register your models here.
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'status', 'created_at', 'description']
    list_display_links = ['task']
    list_filter = ['status']
    search_fields = ['task']
    fields = ['task', 'status', 'created_at']


admin.site.register(Task, TaskAdmin)
