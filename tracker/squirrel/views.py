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
    #age
    cursor = connection.cursor()
    query = """select age,count(*)
               from squirrel_squirrel
               group by age"""
    cursor.execute(query)
    result = cursor.fetchall()
    dict_1=dict()
    dict_1[result[2][0]] = result[2][1]
    dict_1[result[3][0]] = result[3][1]
    dict_1['Unknown'] = result[0][1] + result[1][1]

    #primary fur color
    cursor = connection.cursor()
    query = """select pri_color,count(*)
               from squirrel_squirrel
               group by pri_color"""
    cursor.execute(query)
    result = cursor.fetchall()
    dict_2=dict()
    dict_2[result[1][0]] = result[1][1]
    dict_2[result[2][0]] = result[2][1]
    dict_2[result[3][0]] = result[3][1]
    dict_2['Unknown'] = result[0][1]

    #location
    cursor = connection.cursor()
    query = """select location,count(*)
               from squirrel_squirrel
               group by location"""
    cursor.execute(query)
    result = cursor.fetchall()
    dict_3=dict()
    dict_3[result[1][0]] = result[1][1]
    dict_3[result[2][0]] = result[2][1]
    dict_3['Unknown'] = result[0][1]
    #for i in range(len(result)):
        #dict_3[result[i][0]]=result[i][1]
    
    #activities
    cursor = connection.cursor()
    query = """select count(*) as total_sightings, sum(running) as running, sum(chasing) as chasing,
               sum(climbing) as climbing, sum(eating) as eating, sum(foraging) as foraging,
               sum(kuks) as kuks, sum(quaas) as quaas, sum(moans) as moans, sum(tail_flags) as tail_flags,
               sum(tail_twitches) as tail_twitches
               from squirrel_squirrel"""
    cursor.execute(query)
    names = [i[0] for i in cursor.description]
    result = cursor.fetchone()
    dict_4 = dict()
    for i in range(len(names)):
        dict_4[names[i]] = result[i]


    return render(request,'squirrel/stats.html',locals())

