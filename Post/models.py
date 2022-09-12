from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_ckeditor_5.fields import CKEditor5Field
import datetime


# Create your models here.

from django.db import models

def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    album = instance.album.name
    return f'post/images/{name}/{album}/images/{filename}'

class Category(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    image = models.ImageField(null=True, blank=True,upload_to="post/images/category")
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=255,null=True,unique = True)

    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)
    def __str__(self):
        return self.name

   

@receiver(post_save,sender=Album)
def create_post(sender,instance,created,**kwargs):
    if created:
        post.objects.create(album=instance, title=instance.name, date_created=(datetime.datetime.now()), last_edit_date=(datetime.datetime.now()))
        

@receiver(post_save,sender=Album)
def update_post(sender,instance,created,**kwargs):
    if created == False:
        instance.post.save()
        


class Image(models.Model):
    order = models.FloatField(null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
  
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    def __int__(self):
        return self.order

class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="the_author",
        on_delete=models.CASCADE,)
    
    title=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to=f"post/images/authors")

    def __str__(self):
        return self.user.username


class post(models.Model):

    title= models.CharField(max_length=200,null=True,blank=True)
    date_created= models.DateField(null=True,blank=True)
    last_edit_date= models.DateField(null=True,blank=True)
    author = models.ForeignKey(Author, null=True,blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    text= CKEditor5Field('Text', config_name='extends',null=True,blank=True) 
    HomePage=models.BooleanField(default=False)
    FeaturedPost=models.BooleanField(default=False)
    album = models.OneToOneField(Album, related_name='model', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title