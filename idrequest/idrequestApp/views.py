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
from django.conf import settings

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
        return render(request,'idrequestApp/firstview.html')
    elif request.user.is_authenticated and request.user.userType == 'F' :
        return render(request,'idrequestApp/firstview.html')
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
            fname=request.POST.get('fname')
            fmiddlename=request.POST.get('fmiddlename')
            flastname=request.POST.get('lfastname')
            fnum=request.POST.get('fnumber')
            date=request.POST.get('date')
            gsis=request.POST.get('gsis')
            gpn=request.POST.get('gpn')
            philhealth=request.POST.get('philhealth')
            tin=request.POST.get('tin')
            pagibig=request.POST.get('pagibig')
            fcperson=request.POST.get('fcperson')
            fcnumber=request.POST.get('fcnumber')
            faddress=request.POST.get('address')
            idpic=request.POST.get('idpic')
            signature=request.POST.get('signature')
        
        try:
            datas = facultytable.objects.create(fname=fname, fmiddlename=fmiddlename, flastname=flastname, fnum=fnum, gsis=gsis, gpn=gpn, philhealth=philhealth, tin=tin, pagibig=pagibig, fcperson=fcperson, fcnumber=fcnumber, faddress=faddress, idpic=idpic, signature=signature, date=date, status = 'pending')
            datas.save()
            return redirect('/cfac')
        except:
            print("error")
        return render(request,'idrequestApp/facultyform.html')
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
        return render(request,'idrequestApp/faculty Pending.html')
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
        return render(request,'idrequestApp/Faculty Approved.html')
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
    if request.user.is_authenticated and request.user.userType == 'A':
        return render(request,'idrequestApp/check-faculty.html')
    return redirect('/index')

@login_required(login_url='/index')
def deletestudent (request):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.last()
        check.delete()
        return render(request,'idrequestApp/studentform.html')
    return redirect('/index')

@login_required(login_url='/index')
def viewstudent (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(user_id_id=id)
        return render(request,'idrequestApp/view-student.html', {'check':check})
    return redirect('/index')

def sdelete (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        
      
        check = studenttable.objects.get(user_id_id=id)
        
        send_mail(
    'TUP-CAVITE ID Request: DECLINED',
    'Your request has been declined. Please fill up the form again.',
    'idrequestapp@gmail.com',
    [check.email],
    fail_silently=False,
)
        # send_mail(subject = subject, message =message, auth_user = settings.EMAIL_HOST_USER, recipient_list=[email], fail_silently = false )
        check.delete()
        return redirect('/studentpending')
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
def student (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(id=id)
        return render(request,'idrequestApp/view-student.html', {'check':check})
    return redirect('/index')

@login_required(login_url='/index')
def printstudent (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(user_id_id=id)
        return render(request,'idrequestApp/print-student.html', {'check':check})
    return redirect('/index')




    