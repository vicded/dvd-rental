from django.http import HttpResponse
from django.shortcuts import render

from .models import Actors


# Create your views here.
def actor_template(request):
    return HttpResponse('This is going to be my template')

