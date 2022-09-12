

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(post)
admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Tag)