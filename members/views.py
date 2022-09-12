from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from .forms import loginform



def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('Post:home'))
            # Redirect to a success page.

        else:
            messages.success(request,("There Was A Error Logging In...Try Again.."))
            return redirect(reverse_lazy(('members:login')))

    else:
        form = loginform



        return render(request, 'authenticate/login.html',{'form':form})
