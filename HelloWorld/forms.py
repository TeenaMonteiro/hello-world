from django import forms
from HelloWorld.models import Users




class loginForm(forms.ModelForm):
  
    username=forms.CharField(label="Username",required=True) 

    class Meta:
        model = Users
        exclude = ('user_create_date')  
      
   
