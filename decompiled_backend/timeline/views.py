from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
def index(request):
    if request.user.is_authenticated:
        return render(request,'timeline.html')
    else:
        return ('url login')
