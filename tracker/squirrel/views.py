from .models import Squirrel
from django.shortcuts import render 
from django.shortcuts import redirect
from .forms import SquirrelForm
from django.db import connection

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
    if request.method=='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrel/sightings')
    else:
        form = SquirrelForm()

    return render(request,'squirrel/edit.html',{'form':form})

def update(request, squirrel_id):
    squirrel = Squirrel.objects.filter(squirrel_id=squirrel_id).first()
    #squirrel = Squirrel.objects.get(squirrel_id=squirrel_id)
    if request.method == 'POST':
        #check form data
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrel/sightings')
    else:
        form = SquirrelForm(instance=squirrel)
    return render(request,'squirrel/edit.html',{'form':form})

def stats(request):
    cursor = connection.cursor()
    query = """select age,count(*)
               from squirrel_squirrel
               group by age"""
    cursor.execute(query)
    result = cursor.fetchall()
    dict_1=dict()
    for i in range(len(result)):
        dict_1[result[i][0]]=result[i][1]
    return render(request,'squirrel/stats.html',locals())

