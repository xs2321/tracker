from django.http import HttpResponse,HttpResponseRedirect
from .models import Squirrel
from django.shortcuts import render 
from .forms import SquirrelForm 
def all_sightings(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'squirrel/map.html', context)
# Create your views here.

def all_squirrels(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'squirrel/sightings.html', context)

def add(request):
    form = SquirrelForm(request.POST)
    if form:
        if form.is_valid():
            form.save()
            return redirect('all_squirrels')
    else:
        return render(request,'squirrel/add.html',{'form',form})
