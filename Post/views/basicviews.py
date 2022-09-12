from webbrowser import get
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from requests import post
from Post.forms import *
from django.contrib import messages
import datetime
from Post.filters import OrderFilter
from Post.models import post, Author,Album
# Create your views here.

def home(request):
    featured=post.objects.filter(HomePage=True).select_related('album')   
    context = {'featured':featured}
    return render(request, 'home.html', context)

def post_view(request,post_id):
   thepost=get_object_or_404(post.objects.select_related('author'),pk=post_id)

   return render(request, 'post_view.html', {'post':thepost})

def posthome(request):
   
 
    
    items = post.objects.all().order_by('-date_created')
    print(items)
    myFilter = OrderFilter(request.GET, queryset=items)  
    featured=post.objects.filter(FeaturedPost=True)
    posts = myFilter.qs
    tagform = checkboxtags()
    context = {'posts':posts, 'myFilter':myFilter,'tagform':tagform,'featured':featured}
    return render(request, 'post_home.html',context)


   