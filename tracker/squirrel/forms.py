from django import forms
from .models import Squirrel

class SquirrelForm(forms.ModelForm):
    class IndividualSquirrel:
        model = Squirrel
        field = [
                "lon",
                "lat",
                "squirrel_id",
                "shift",
                "age",
                "pri_color",
                "location",
                "specific_location",
                "running",
                "chasing",
                "climbing",
                "eating",
                "foraging",
                "other_activities",
                "kuks",
                "quaas",
                "moans",
                "tail_flags",
                "tail_twitches",
                "approaches",
                "indifferent",
                "runs_from",
                ]

