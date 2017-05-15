from django.shortcuts import render

from .models import *


def index_view(request):
    conferences = Event.objects.all()
    context = {"conference": conferences}
    template = 'index.html'

    return render(request, template, context)


def event_view(request):
    context = {}
    template = 'event.html'

    return render(request, template, context)


def single_conference(request, id):
    conference = Event.objects.get(id=id)
    speakers = Personal.objects.filter(conference=conference)

    context = {"item": conference, "speakers": speakers}
    template = 'event.html'

    return render(request, template, context)
