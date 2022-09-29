from ast import main
from multiprocessing import context
from ssl import HAS_TLSv1_1
from turtle import title
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from dataclasses import dataclass
from typing import List
# Create your views here.

@dataclass 
class Team:
    title: str
    members: list[str]
    desc: str



teams = { 
    "Management": Team("Management Team",["Kevin,", "Andrew,", "Lukas,", "Chevy,", "Brooks,", "& Errin"], "Management Team is important to keep every group in order. This team is there to provide extra support where it is needed."),
    "Documentation": Team("Documentation Team", ["Cannon,", "Gabbi,", "Cooper,", "Isaiah,", "Colt,", "Antonio,", "& Angela"], "Documentation is at Base Camp to document everything. Documentation works with a variety of media types to spread the word about Base Camp's activities. Documentation is helpful in getting the word out to future employers who may need a new employee."),
    "Procurement": Team("Procurement Team", ["Mike,", "Zaul,", "Dylan,", "River,", "Luke,", "& Anna"], "Procurement Team gathers all of the food needed at Base Camp to feed 30 people. Their work helps cut down the cost of a meal for each student. They help provide daily meals."),
    "Community": Team("Community Team", ["Eric,", "JW,", "Joshua,", "Amber,", "& Malcolm"], "Community Team's job is to source events for Base Camp to insert themselves into. This can range from relaxing activities to career focused events.")
}


def index(request):
    context={
    "lp":["Management", "Documentation", "Procurement", "Community"]}
    return render(request, "index.html", context)

def details(request, team_name):
    team_name = teams[team_name]
    context = {
        "title": team_name.title,
        "members": team_name.members,
        "desc": team_name.desc
    }

    return render(request, "details.html", context )