from django.forms.widgets import CheckboxSelectMultiple
from django import forms

from .models import *

from django.forms.models import ModelForm





class PostForm(forms.ModelForm):
    
	class Meta:
      
		model = post
		
       
		fields = ('title','author','category','tags','text','album','HomePage','FeaturedPost')				
		labels = {
			'title':'Title',
			'author':'Author',
			'category':'Category',
			'text':'Text',
			'tags': 'Tags',
			'date_created':'Date Created',
			'album':"Album",
            'HomePage':'Home Page',
			'FeaturedPost':'Featured Post',
		}
	
		
		
	def __init__(self, *args, **kwargs):
			
			super(PostForm, self).__init__(*args, **kwargs)
			
			self.fields["tags"].widget = CheckboxSelectMultiple()
			self.fields["tags"].queryset = Tag.objects.all()
		

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ('order','description','image','default')
		labels = {
			'order':'Order',
			'description':'Description',
			'image':'Image',
			'default':'Default',
		}
		
	def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['order'].widget.attrs.update({'placeholder': '1,2,3..'})
			self.fields['description'].widget.attrs.update({'placeholder': 'Brief Description'})
		
    		
      
class NewPostForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ('__all__')

class checkboxtags(forms.Form):
	
	tags = forms.ModelMultipleChoiceField(
		queryset=Tag.objects.all(),
		to_field_name='id',
		widget=forms.CheckboxSelectMultiple()
		)
		
	