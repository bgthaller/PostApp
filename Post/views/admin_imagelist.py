from django.contrib.auth.decorators import login_required
from Post.decorators import allowed_users
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from Post.forms import *
import os
from Post.models import post, Author,Album

@login_required
@allowed_users(allowed_roles=['Editor'])
def imageList(request, id):
    if request.method == "GET":        
        form = ImageForm
        images=Image.objects.filter(album=id).all()
        context = {'images':images,'form':form}
    
        return render(request, 'imageList.html',context)
    else:
        form = new_func(request)
        if form.is_valid():
            udate=form.save(commit=False)
            addalbum=Album.objects.get(id=id)
            udate.album = addalbum
            udate.save()           
            print("image saved")
        else:
            print("image not saved")
            print(form.errors)
        images=Image.objects.filter(album=id).all()
        form=ImageForm
        context = {'images':images,'form':form}
        return redirect(reverse_lazy('Post:imageList', kwargs={'id': id}),context)

@login_required
@allowed_users(allowed_roles=['Editor'])
def new_func(request):
    #need request.FILES for images
    form = ImageForm(request.POST,request.FILES)
    return form

@login_required
@allowed_users(allowed_roles=['Editor'])
def image_delete(request,id):
    selected_image = Image.objects.get(pk=id)
    curalbum = selected_image.album.id
    selected_image.delete()
    print(curalbum)
    return redirect(reverse_lazy('Post:imageList', kwargs={'id': curalbum}))

@login_required
@allowed_users(allowed_roles=['Editor'])    
def image_update(request, id=0):
    #if we are trying to view edit page. If new just show blank form, else show form with 
    # current data in it
    imageupdate= Image.objects.get(pk=id) 
    old_image_path = imageupdate.image.path
   

    if request.method == "GET":               
        curalbum = imageupdate.album.id  # used to get id for link to return to images in album        
        form = ImageForm(instance=imageupdate)
        context = {'curalbum':curalbum,'form':form}
        return render(request, 'edit_image.html', context)
    #from the form page we hit submit
    else:   
        # editing a existing image    
        
        curalbum = imageupdate.album.id
        form = ImageForm(request.POST,request.FILES, instance = imageupdate)
   
        if form.is_valid():         
             # deleting old uploaded image.
            image_path = imageupdate.image.path
            print(old_image_path)
            print(image_path)
            if os.path.exists(old_image_path):
                if old_image_path != image_path:
                    print("deleting old image")
                    os.remove(old_image_path)          
            update=form.save(commit=False)
            update.album = imageupdate.album            
            update.save()
            
            
        else:
           
            print(form.errors)
            return render(request, 'edit_image.html',{'form':form})
        
        return redirect(reverse_lazy('Post:imageList', kwargs={'id': curalbum}))