from ast import main
from multiprocessing import context
from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from dataclasses import dataclass
# Create your views here.

@dataclass 
class Team:
    title: str
    members: List[str]
    desc: str



def 


    return render(request, "base.html", context)