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


class ApplicationAdmin(admin.ModelAdmin):
    class Meta:
        model = Application

    list_display = ['name', 'conference', 'email']


class FeedBackAdmin(admin.ModelAdmin):
    class Meta:
        model = Feedback

admin.site.register(Feedback, FeedBackAdmin)

admin.site.register(Application, ApplicationAdmin)

admin.site.register(Event, EventAdmin)

admin.site.register(Personal, PersonAdmin)
