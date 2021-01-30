from django import forms  
from .models import RouterDetails

class RouterForm(forms.ModelForm):  
    class Meta:  
        model = RouterDetails 
        fields = "__all__" 