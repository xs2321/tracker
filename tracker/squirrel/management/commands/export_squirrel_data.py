import csv
from squirrel.models import Squirrel
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help='Export Squirrel Data'
    
    def add_arguments(self,parser):
        parser.add_argument('path',type=str)
    

    def handle(self, *args,**kwargs):
        path = kwargs['path']
        from django.apps import apps
        model = apps.get_model('squirrel', 'Squirrel')
        field_names = [f.name for f in model._meta.fields]
        with open(path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, f) for f in field_names])
