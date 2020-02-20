from django.contrib import admin

from .models import Task, TaskTracker


admin.site.register(Task)
admin.site.register(TaskTracker)
