from django.http import HttpResponse
from django.shortcuts import render
from .models import * 

# Create your views here.
def index(request):
    return render(request, "tasks/index.html")