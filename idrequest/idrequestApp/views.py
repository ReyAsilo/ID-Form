from django.http.response import FileResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from idrequestApp.forms import sform,fform
from .models import studenttable
from .models import facultytable


# Create your views here.
def index (request):
    return render(request,'idrequestApp/index.html')
def pick (request):
    return render(request,'idrequestApp/pick.html')
def forms (request):
    if request.method == 'POST':
        name=request.POST.get('firstname')
        middlename=request.POST.get('middle')
        lastname=request.POST.get('lastname')
        section=request.POST.get('section')
        idnum=request.POST.get('idnum')
        cname=request.POST.get('cname')
        cnumber=request.POST.get('cnumber')
        add=request.POST.get('address')
        pic=request.POST.get('pic')
        signature=request.POST.get('signature')
        date=request.POST.get('date')
    try:
        datas = studenttable.objects.create(name=name, middlename=middlename, lastname=lastname, course=section, snumber=idnum, cperson=cname, 
        cnumber=cnumber, address=add, idpic=pic, signature=signature, date=date, status = 'pending')
        datas.save()
        return redirect('/cstud')
    except:
        print("error")
        return render(request, 'idrequestApp/sform.html')
    return render(request, 'idrequestApp/sform.html')
def cstud (request):
    check = studenttable.objects.last()
    return render(request,'idrequestApp/cstud.html', {'check':check})
def fform (request):
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
        others=request.POST.get('others')
        fcperson=request.POST.get('fcperson')
        fcnumber=request.POST.get('fcnumber')
        faddress=request.POST.get('address')
        idpic=request.POST.get('idpic')
        signature=request.POST.get('signature')
        
    try:
        datas = facultytable.objects.create(fname=fname, fmiddlename=fmiddlename, flastname=flastname, fnum=fnum, gsis=gsis, gpn=gpn, philhealth=philhealth, tin=tin, pagibig=pagibig, others=others, fcperson=fcperson, fcnumber=fcnumber, faddress=faddress, idpic=idpic, signature=signature, date=date, status = 'pending')
        datas.save()
        return redirect('/cfac')
    except:
        print("error")
    return render(request,'idrequestApp/fform.html')
def cfac (request):
    return render(request,'idrequestApp/cfac.html')
def pending (request):
    display = studenttable.objects.filter(status='pending')
    return render(request,'idrequestApp/pending.html', {'display':display})

def view_details(request, id):
    student = studenttable.objects.get(id=id)
    print("rey")
    return render(request, 'sapproval.html', {'student':student})


def sapproval (request):
    return render(request,'idrequestApp/sapproval.html')
def fapproval (request):
    return render(request,'idrequestApp/fapproval.html')
def approved (request):
    return render(request,'idrequestApp/approved.html')
def declined (request):
    return render(request,'idrequestApp/declined.html')
def sinfo (request):
    return render(request,'idrequestApp/sinfo.html')
def finfo (request):
    return render(request,'idrequestApp/finfo.html')

    


