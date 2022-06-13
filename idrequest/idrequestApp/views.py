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
            photo = studenttable()
            photo.name=request.POST.get('name')
            photo.middlename=request.POST.get('middlename')
            photo.lastname=request.POST.get('lastname')
            photo.course=request.POST.get('section')
            photo.snumber=request.POST.get('idnum')
            photo.cperson=request.POST.get('cname')
            photo.cnumber=request.POST.get('cnumber')
            photo.address=request.POST.get('address')
            photo.status = 'pending'
            if len(request.FILES) != 0:
                photo.idpic = request.FILES['pic']
                photo.signature = request.FILES['signature']
            photo.save()
            
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
            form.save()
            return redirect ('/index')
    context =  {'form': form }
    return render(request, 'idrequestApp/registration.html', context)
    

@login_required(login_url='/index')
def checkstudent (request):
    if request.user.is_authenticated and request.user.userType == 'A':
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
        check = studenttable.objects.get(id=id)
        return render(request,'idrequestApp/view-student.html', {'check':check})
    return redirect('/index')

def sdelete (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(id=id)
        check.delete()
        return redirect('/studentpending')
    return redirect('/index')

@login_required(login_url='/index')
def appstudent (request, id):
    if request.user.is_authenticated and request.user.userType == 'A':
        check = studenttable.objects.get(id=id)
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
        check = studenttable.objects.get(id=id)
        return render(request,'idrequestApp/print-student.html', {'check':check})
    return redirect('/index')




    