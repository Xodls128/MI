from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'color', 'created_at')
    search_fields = ('title', 'description', 'content')
    list_filter = ('start_time', 'end_time', 'color')

admin.site.register(Event, EventAdmin)
