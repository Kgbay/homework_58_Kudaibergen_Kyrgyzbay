from django.contrib import admin

from .models import Task, Status
from .models import Type


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('summary', 'description', 'created_at', 'status', 'type')
    list_filter = ('id', 'summary', 'created_at')
    search_fields = ('summary', 'description', 'created_at', 'updated_at')
    fields = ('summary', 'description', 'status', 'type')
    readonly_fields = ('id', 'updated_at')


admin.site.register(Task, TaskAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'created_at')


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('status_name', 'created_at')


admin.site.register(Status, StatusAdmin)
