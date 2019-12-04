from django.http import HttpResponse
from .models import Squirrel
from django.shortcuts import render

def all_sightings(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'squirrel/map.html', context)
# Create your views here.
