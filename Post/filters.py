
from django.forms import DateInput
import django_filters
from Post.models import *
from django.forms.widgets import CheckboxSelectMultiple

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = post
        fields =('__all__')
        exclude = ['date_created','last_edit_date','text','author','title','HomePage','FeaturedPost','album']
    date = django_filters.DateFilter(
    widget=DateInput(
        attrs={
            'type' : 'date',
            'class': 'hasDatePicker'
        }
    )
)
   
        
       

    
    

      
    


