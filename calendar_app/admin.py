from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'backgroundColor')
    search_fields = ('title', 'description')
    list_filter = ('start_time', 'end_time', 'backgroundColor')

admin.site.register(Event, EventAdmin)
