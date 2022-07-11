from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings

app_name='idrequestApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('logout/', views.logoutUser, name= 'logout'),
    path('pick/',views.pick, name='pick'),
    path('forms/',views.forms, name='forms'),
    
    path('fforms/',views.fforms, name='fforms'),
    
 

    path('registration/',views.newreg, name='newreg'),
    
    path('studentpending/',views.studentpending, name='studentpending'),
    path('facultypending/',views.facultypending, name='facultypending'),
    
    path('studentapproved/',views.studentapproved, name='studentapproved'),
    path('facultyapproved/',views.facultyapproved, name='facultyapproved'),
    
    path('checkstudent/',views.checkstudent, name='checkstudent '),
    path('checkfaculty/',views.checkfaculty, name='checkfaculty'),
    
    path('deletestudent/', views.deletestudent, name='deletestudent'),
    path('deletefaculty/', views.deletefaculty, name='deletefaculty'),
    
    
    path('viewstudent/<int:id>', views.viewstudent, name='viewstudent'),
    path('viewfaculty/<int:id>', views.viewfaculty, name='viewfaculty'),
    
    
    
    path('sdelete/<int:id>', views.sdelete, name='sdelete'),
    path('fdelete/<int:id>', views.fdelete, name='fdelete'),
    
    
    path('appstudent/<int:id>', views.appstudent, name='appstudent'),
    path('appfaculty/<int:id>', views.appfaculty, name='appfaculty'),
    
    path('fpdf/<int:id>',views.fpdf, name ='fpdf'),
    path('pdf/<int:id>', views.pdf , name='pdf'),
    
    
    
  
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)