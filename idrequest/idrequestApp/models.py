from django.db import models
import datetime
import os
from email.policy import default
import os
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.

class registration(AbstractUser):
    
    
    userType = [
        ('S', 'Student'),
        ('F', 'Faculty'),
        ('A', 'Admin'),
        
        ]
    userType = models.CharField(max_length=30, choices= userType, verbose_name='userType', default ='S')
    

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now() .strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)
    
    
    
    
   
class studenttable(models.Model):
    CHOICES = [('COET', 'Computer Engineering Technology'),('BSIE', 'BS Industrial Education')
    ]
    name = models.CharField(max_length=200, blank=True, null=True)
    middlename = models.CharField(max_length=200, blank=True, null=True)
    lastname = models.CharField(max_length=200, blank=True, null=True)
    course =  models.CharField(max_length=200, choices=CHOICES)
    snumber = models.CharField(max_length=200, blank=True, null=True)
    cperson = models.CharField(max_length=200, blank=True, null=True)
    cnumber = models.IntegerField ( blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    idpic = models.ImageField(blank=True, null=True, upload_to=filepath)
    signature = models.ImageField(blank=True, null=True, upload_to=filepath)
    status = models.CharField(max_length=200, blank=True, null=True)


class facultytable(models.Model):
    fname = models.CharField(max_length=200, blank=True, null=True)
    fmiddlename = models.CharField(max_length=200, blank=True, null=True)
    flastname = models.CharField(max_length=200, blank=True, null=True)
    fnumber = models.CharField(max_length=200, blank=True, null=True) 
    date = models.CharField(max_length=200, blank=True, null=True) 
    gsis = models.IntegerField ( blank=True, null=True)
    gpn =models.IntegerField ( blank=True, null=True)
    philhealth = models.IntegerField ( blank=True, null=True)
    tin = models.IntegerField ( blank=True, null=True)
    pagibig =models.IntegerField (blank=True, null=True)
    fcperson = models.CharField(max_length=200, blank=True, null=True)
    fcnumber = models.IntegerField ( blank=True, null=True)
    faddress = models.CharField(max_length=200, blank=True, null=True)
    idpic = models.ImageField(blank=True, null=True, upload_to="img/%y")
    signature = models.ImageField(blank=True, null=True, upload_to="img/&y ")
    status = models.CharField(max_length=200, blank=True, null=True)



