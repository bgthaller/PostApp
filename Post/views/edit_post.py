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
def editpost(request, id=0):
    #if we are trying to view edit page. If new just show blank form, else show form with 
    # current data in it
    if request.method == "GET":
        if id == 0:
            form = PostForm
        else:
            postupdate= post.objects.get(pk=id)
            form = PostForm(instance=postupdate)
        return render(request, 'edit_post.html', {'form':form})
    #from the form page we hit submit
    else:
        # if a new post
        if id == 0:
            form = PostForm(request.POST)
            
        # editing a existing post    
        else:
            postupdate= post.objects.get(pk=id)
            form = PostForm(request.POST, instance = postupdate)
        
        if form.is_valid():
            print('saved')
            settime=form.save(commit=False)           
            settime.last_edit_date = (datetime.datetime.now())
            settime.save()
            # must save m2m field seperalty after using commit = False
            form.save_m2m()
        else:
            print('did not save')
            print(form.errors)
             
            return render(request, 'edit_post.html',{'form':form})
        
        return redirect(reverse_lazy('Post:admin_postlist'))