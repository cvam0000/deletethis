from django.shortcuts import render,redirect

from . import bot


def index(request):
    if request.user.is_authenticated:
    	
    	return 0


    else:
        a=redirect('login')
        return a





