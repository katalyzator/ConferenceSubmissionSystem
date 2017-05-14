from django.contrib import admin

from .models import *


class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event

    list_display = ['title', 'description', 'start', 'finish']


class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = Personal

    list_display = ['conference', 'name', 'position']


admin.site.register(Event, EventAdmin)

admin.site.register(Personal, PersonAdmin)
