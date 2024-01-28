from django import forms 
from. models import Blog

class Edite_Blog(forms.ModelForm):
    class Meta:
            model = Blog
            fields=('title','dsc')
