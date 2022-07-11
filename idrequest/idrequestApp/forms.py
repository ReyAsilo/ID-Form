import email
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import facultytable, registration, studenttable


class UserRegistration(UserCreationForm):
    class Meta:
        model = registration
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'userType']
        widgets = {
            'first_name' : forms.TextInput(attrs ={'class':'form-control'} ),
            'last_name' : forms.TextInput(attrs ={'class':'form-control'} ), 
            'email' : forms.EmailInput(attrs ={'class':'form-control'} ),
            'username' : forms.TextInput(attrs ={'class':'form-control'} ),
            'userType' : forms.Select(attrs ={'class':'form-control'} ),
        }











class sform(forms.ModelForm):  
    class Meta:  
        model = studenttable
      
        fields = ['name', 'middlename', 'lastname', 'course', 'snumber', 'cperson', 'cnumber', 'address', 'idpic', 'signature', 'email']

class fform(forms.ModelForm):
    class Meta:
        model = facultytable

        fields = ['name', 'middlename', 'lastname', 'fnumber', 'gsis', 'gpn', 'philhealth', 'tin', 'pagibig', 'cperson', 'cnumber', 'address', 'idpic', 'signature' ]

