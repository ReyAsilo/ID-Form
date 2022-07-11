from pyexpat.errors import messages
from django.http.response import FileResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from idrequestApp.forms import sform,fform 
from .models import studenttable
from .models import facultytable
from .models import registration
from django.contrib import messages
import mysql.connector as sql
from .forms import UserRegistration
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.views.generic import View
from .process import html_to_pdf 



# Create your views here.
def index (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password) 
        print(user)

        if user is not None and user.userType == 'S':
            login(request, user)
            return redirect('/pick')
        elif user is not None and user.userType == 'F':
            login(request, user)
            return redirect('/pick')

        elif user is not None and user.userType == 'A':
            login(request, user)
            return redirect('/studentpending')       
         
    return render(request,'idrequestApp/index.html')

def logoutUser(request):
    logout(request)
    return redirect('/index')

@login_required(login_url='/index')
def pick (request):
    if request.user.is_authenticated and request.user.userType == 'S' :
        idd = request.user.id
        check = registration.objects.get(id = idd)
        checkk = studenttable.objects.get(user_id = idd)
        
        if checkk.status == 'pending':
            return render(request,'idrequestApp/firstviews.html', {'check':check})
        
        elif checkk.status == 'approved':
            return render(request,'idrequestApp/firstviewss.html', {'check':check})
        
        else:
            return render(request,'idrequestApp/firstview.html', {'check':check})
    
    
    elif request.user.is_authenticated and request.user.userType == 'F':
        idd = request.user.id
        check = registration.objects.get(id = idd)
        checkk = facultytable.objects.get(user_id = idd)
        
        if checkk.status == 'pending':
            return render(request,'idrequestApp/firstviews.html', {'check':check})
        
        elif checkk.status == 'approved':
                return render(request,'idrequestApp/firstviewss.html', {'check':check})
        
        else:
             return render(request,'idrequestApp/firstview.html', {'check':check})
    
    return redirect('/index')

@login_required(login_url='/index')
def forms (request):
    if request.user.is_authenticated and request.user.userType == 'S':
        
        
        if request.method == 'POST':      
            
            student = studenttable.objects.get(user_id_id = request.user.pk)
          
            student.name=request.POST.get('name')
            student.middlename=request.POST.get('middlename')
            student.lastname=request.POST.get('lastname')
            student.course=request.POST.get('section')
            student.snumber=request.POST.get('idnum')
            student.cperson=request.POST.get('cname')
            student.cnumber=request.POST.get('cnumber')
            student.address=request.POST.get('address')
            student.email = request.POST.get('email')
            student.status = 'pending'
            if len(request.FILES) != 0:
                student.idpic = request.FILES['pic']
                student.signature = request.FILES['signature']
            student.save()
            return redirect('/checkstudent')
        else:
            print("error")
            return render(request, 'idrequestApp/studentform.html')
            
    return redirect('/pick')


@login_required(login_url='/index')
def fforms (request):
    if request.user.is_authenticated and request.user.userType == 'F':
        if request.method == 'POST':
            faculty = facultytable.objects.get(user_id_id = request.user.pk)
          
            faculty.name=request.POST.get('name')
            faculty.middlename=request.POST.get('middlename')
            faculty.lastname=request.POST.get('lastname')

            faculty.fnumber=request.POST.get('employee')
            faculty.gpn=request.POST.get('gsis')
            faculty.gpn=request.POST.get('gpn')
            faculty.philhealth=request.POST.get('philhealth')
            faculty.tin=request.POST.get('tin')
            faculty.pagibig=request.POST.get('pagibig')
            
            
            faculty.cperson=request.POST.get('cperson')
            faculty.cnumber=request.POST.get('cnumber')
            faculty.address=request.POST.get('address')

            faculty.status = 'pending'
            if len(request.FILES) != 0:
                faculty.idpic = request.FILES['pic']
                faculty.signature = request.FILES['signature']
            faculty.save()
            return redirect('/checkfaculty')
        else:
            print("error")
            return render(request, 'idrequestApp/facultyform.html')
    return redirect('/pick')



def newreg (request):
    return render(request,'idrequestApp/registration.html')


@login_required(login_url='/index')
def studentpending (request):
    if request.user.is_authenticated and request.user.userType == 'A':
        display = studenttable.objects.filter(status='pending')
        context = {'display':display}
        return render(request,'idrequestApp/Student Pending.html', context)
    return redirect('/index')

@login_required(login_url='/index')
def facultypending (request):
    if request.user.is_authenticated and request.user.userType == 'A':
        display = facultytable.objects.filter(status='pending')
        context = {'display':display}
        return render(request,'idrequestApp/faculty Pending.html', context)
    return redirect('/index')

@login_required(login_url='/index')
def studentapproved (request):
    if request.user.is_authenticated and request.user.userType == 'A':
        display = studenttable.objects.filter(status='approved')
        context = {'display':display}
        return render(request,'idrequestApp/Student Approved.html', context)
    return redirect('/index')

@login_required(login_url='/index')
def facultyapproved (request):
    if request.user.is_authenticated and request.user.userType == 'A':   
        display = facultytable.objects.filter(status='approved')
        context = {'display':display} 
        return render(request,'idrequestApp/Faculty Approved.html', context)
    return redirect('/index')

def newreg (request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data.get('username')
            user = form.cleaned_data.get('userType')
            form.save()
            
            if user == 'S':
                new = registration.objects.get(username = username1)
                studenttable.objects.create(user_id = new)
            if user == 'F':
                new = registration.objects.get(username = username1)
                facultytable.objects.create(user_id = new)
                
        return redirect ('/index')
                 
    context =  {'form': form }
    return render(request, 'idrequestApp/registration.html', context)
    

@login_required(login_url='/index')
def checkstudent (request):
    if request.user.is_authenticated and request.user.userType == 'S':
        check = studenttable.objects.last()
        return render(request,'idrequestApp/check-student.html', {'check':check})
    return redirect('/index')

@login_required(login_url='/index')
def checkfaculty (request):
    if request.user.is_authenticated and request.user.userType == 'F':
        check = facultytable.objects.last()
        return render(request,'idrequestApp/check-faculty.html', {'check':check})
    return redirect('/index')

@login_required(login_url='/index')
def deletestudent (request):
    if request.user.is_authenticated and request.user.userType == 'S':
        check = studenttable.objects.last()
        check.delete()
        return render(request,'idrequestApp/studentform.html')
    return redirect('/index')


@login_required(login_url='/index')
def deletefaculty (request):
    if request.user.is_authenticated and request.user.userType == 'F':
        check = facultytable.objects.last()
        check.delete()
        return render(request,'idrequestApp/facultyform.html')
    return redirect('/index')


@login_required(login_url='/index')
def viewstudent (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(user_id_id=id)
        return render(request,'idrequestApp/view-student.html', {'check':check})
    return redirect('/index')



@login_required(login_url='/index')
def viewfaculty (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = facultytable.objects.get(user_id_id=id)
        return render(request,'idrequestApp/view-faculty.html', {'check':check})
    return redirect('/index')

def sdelete (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        
        check = studenttable.objects.get(user_id_id=id)
        
        send_mail(
    'TUP-CAVITE ID Request: DECLINED',
    'Your request has been declined. Please fill up the form again.',
    'TUPC-ID Request',
    [check.email],
    fail_silently=False,
)
      
        check.status = "declined"
        check.save()
    
        return redirect('/studentpending')
    return redirect('/index')


@login_required(login_url='/index')
def fdelete (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        checkk = registration.objects.get(id=id)
        check = facultytable.objects.get(user_id_id=id)
     
        send_mail(
            'TUP-CAVITE ID Request: APPROVED',
            'Your request has been declined. Please fill up the form again.',
            'idrequestapp@gmail.com',
            [checkk.email],
            fail_silently=False,)
        
        check.status = "declined"
        check.save()
        return redirect('/facultypending')
    return redirect('/index')

@login_required(login_url='/index')
def appstudent (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(user_id_id=id)
        send_mail(
            'TUP-CAVITE ID Request: APPROVED',
            'Your request has been approved. Please wait for the schedule of picking up your ID.',
            'idrequestapp@gmail.com',
            [check.email],
            fail_silently=False,)
         
        check.status = "approved"
        check.save()
        return redirect('/studentpending')
    return redirect('/index')


@login_required(login_url='/index')
def appfaculty (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        checkk = registration.objects.get(id=id)
        check = facultytable.objects.get(user_id_id=id)
     
        send_mail(
            'TUP-CAVITE ID Request: APPROVED',
            'Your request has been approved. Please wait for the schedule of picking up your ID.',
            'idrequestapp@gmail.com',
            [checkk.email],
            fail_silently=False,)
        
        check.status = "approved"
        check.save()
        return redirect('/facultypending')
    return redirect('/index')



@login_required(login_url='/index')
def student (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(id=id)
        return render(request,'idrequestApp/view-student.html', {'check':check})
    return redirect('/index')




@login_required(login_url='/index')
def pdf (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(user_id_id=id)
        return render(request,'idrequestApp/idpdf.html', {'check':check})
    return redirect('/index')



@login_required(login_url='/index')
def fpdf (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = facultytable.objects.get(user_id_id=id)
        return render(request,'idrequestApp/fidpdf.html', {'check':check})
    return redirect('/index')







    