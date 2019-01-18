from django.shortcuts import render,redirect
from .forms import PostForm
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
import telepot



def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request,'timeline.html',{'posts': posts})
    else:
        a=redirect('login')
        return a


def bot(a):
    if a:
        bot = telepot.Bot('438212244:AAGQ1VhzLHowzxUTFiT6GTirIVxjL3PO79I')
        #po = Post.objects.latest('id')
        po=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        #c=Post.published_date.last()
        #result = [Post.published_date.latest('date_added')]

        text='please confirm for the weekend meet [sunday or (saturday @ null meet)]'


        
        bot.sendMessage(499134543, text )
        #ajx
        bot.sendMessage(680139252, text)
        #mason
        bot.sendMessage(660463343, text)
        #ayan
        bot.sendMessage(400670226, text)
        #alok
        bot.sendMessage(271397625, text)
        #dunken
        bot.sendMessage(399195869, text)
        #math
        bot.sendMessage(407034913, text)
        #bit_bang
        bot.sendMessage(-1001163644641,text)



def post_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                a=1
                bot(a)
                post.save()
                return redirect('timeline')
        else:
            form = PostForm()
            return render(request, 'timeline/form.html', {'form': form})
    else:
        a=redirect('login')
        return a
