from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy


# used to ensure user is in the proper group to run a certian view function
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args, **kwargs)
            else:
                messages.success(request,("You do not have the proper permissions!"))
            return redirect(reverse_lazy(('Post:home')))


        return wrapper_func
    return decorator