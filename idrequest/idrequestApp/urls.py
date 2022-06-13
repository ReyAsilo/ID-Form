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
    
    path('fform/',views.fforms, name='fform'),
    
 

    path('registration/',views.newreg, name='newreg'),
    
    path('studentpending/',views.studentpending, name='studentpending'),
    path('facultypending/',views.facultypending, name='facultypending'),
    
    path('studentapproved/',views.studentapproved, name='studentapproved'),
    path('facultyapproved/',views.facultyapproved, name='facultyapproved'),
    
    path('checkstudent/',views.checkstudent, name='checkstudent '),
    path('checkfaculty/',views.checkfaculty, name='checkfaculty'),
    
    path('deletestudent/', views.deletestudent, name='deletestudent'),
    
    
    path('viewstudent/<int:id>', views.viewstudent, name='viewstudent'),
    path('printstudent/<int:id>', views.printstudent, name='printstudent'),
    
    path('sdelete/<int:id>', views.sdelete, name='sdelete'),
    path('appstudent/<int:id>', views.appstudent, name='appstudent'),
    
  
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)