from django.contrib.auth.decorators import login_required
from Post.decorators import allowed_users
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from Post.forms import *
from django.contrib import messages
import datetime
from Post.filters import OrderFilter

from Post.models import post, Author,Album

@login_required
@allowed_users(allowed_roles=['Editor'])
def admin_postlist(request):
    
   
    if request.method == "GET":
        posts=post.objects.all().order_by('-date_created')
        form=NewPostForm
        return render(request, 'admin_postlist.html', {'posts':posts,'form':form})
    else:
        form = new_func(request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item Created')
            posts=post.objects.all().order_by('-date_created')
            form=NewPostForm
            return redirect(reverse_lazy('Post:admin_postlist'),{'posts':posts,'form':form})
            
        else:  
            print('did not save') 
            print(form.errors)  
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
            posts=post.objects.all().order_by('-date_created')
            form=NewPostForm
            return redirect(reverse_lazy('Post:admin_postlist'),{'posts':posts,'form':form })

@login_required
@allowed_users(allowed_roles=['Editor'])
def new_func(request):
    form = NewPostForm(request.POST)
    return form

@login_required
@allowed_users(allowed_roles=['Editor'])
def post_delete(request,id):
    selected_blog = Album.objects.get(pk=id)
    selected_blog.delete()
    return redirect(reverse_lazy('Post:admin_postlist'))