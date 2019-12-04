from django.urls import path

from . import views

urlpatterns = [
        path('map/', views.all_sightings),
        path('sightings/',views.all_squirrels),
        path('sightings/add/',views.add),
        path('sightings/<squirrel_id>/',views.update),
]
