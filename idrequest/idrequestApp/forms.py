from django import forms 


class sform(forms.ModelForm):  
    class Meta:  
      
        fields = ('name', 'middlename', 'lastname', 'course', 'snumber', 'cperson', 'cnumber', 'address', 'idpic', 'signature', 'date' )

class fform(forms.ModelForm):
    class Meta:

        fields = ('fname', 'fmiddlename', 'flastname', 'fnumber', 'date', 'gisis', 'gpn', 'philhealth', 'tin', 'pagibig', 'others', 'fcperson', 'fcnumber', 'faddress', 'idpic', 'signature' )
        

       