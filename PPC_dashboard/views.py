# Create your views here.
from django.shortcuts import redirect, render

def home(request):
    return render(request, "base.html")