import csv
from squirrel.models import Squirrel
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help='Export Squirrel Data'
    
    def add_arguments(self,parser):
        parser.add_argument('path',type=str)
    

    def handle(self, *args,**kwargs):
        path = kwargs['path']
        with open(path,'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                date = row[5]
                m = date[:2]
                d = date[2:4]
                y = date[4:]
                new_date = y + '-' + m + '-' + d
                p = Squirrel(
                    lon = float(row[0]),
                    lat = float(row[1]),
                    squirrel_id = row[2],
                    shift = row[4],
                    date = new_date,
                    age = row[7],
                    pri_color = row[8],
                    location = row[12],
                    specific_location = row[14],
                    running = self.str_to_bool(row[15]),
                    chasing = self.str_to_bool(row[16]),
                    climbing = self.str_to_bool(row[17]),
                    eating = self.str_to_bool(row[18]),
                    foraging = self.str_to_bool(row[19]),
                    other_activities = row[20],
                    kuks = self.str_to_bool(row[21]),
                    quaas = self.str_to_bool(row[22]),
                    moans = self.str_to_bool(row[23]),
                    tail_flags = self.str_to_bool(row[24]),
                    tail_twitches = self.str_to_bool(row[25]),
                    approaches = self.str_to_bool(row[26]),
                    indifferent = self.str_to_bool(row[27]),
