from django.urls import path

from . import views

urlpatterns = [
        path('map/', views.all_sightings),
        path('sightings/',views.all_squirrels),
        path('sightings/add/',views.add,name='add'),
<<<<<<< HEAD
        path('sightings/stats/',views.stats,name='stats'),
        path('sightings/<squirrel_id>/',views.update,name='update'),
=======
        path('sightings/<squirrel_id>/',views.update,name='update'),
        path('sightings/stats/',views.stats,name='stats'),
>>>>>>> ae7bea478faf5eec8955aa503266b3881b71f8c8
]
