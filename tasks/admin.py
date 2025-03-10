from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'description')

