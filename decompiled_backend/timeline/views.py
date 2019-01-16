from django.shortcuts import render,redirect
from .forms import PostForm
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post
def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request,'timeline.html',{'posts': posts})
    else:
        a=redirect('login')
        return a





def post_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('timeline')
        else:
            form = PostForm()
            return render(request, 'timeline/form.html', {'form': form})
    else:
        a=redirect('login')
        return a
