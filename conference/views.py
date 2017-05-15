from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *


def index_view(request):
    feedbacks = Feedback.objects.all()
    conferences = Event.objects.all()
    context = {"conference": conferences, "feedbacks": feedbacks}
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


@csrf_exempt
def get_application(request, id):
    conference = Event.objects.get(id=id)
    name = request.POST.get('name')
    email = request.POST.get('email')
    number = request.POST.get('number')

    try:

        p = Application(conference=conference, name=name, email=email, number=number)

        p.save()

        return JsonResponse(dict(result=True))
    except:
        return JsonResponse(dict(result=False))
