from django.urls import path
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings

app_name='idrequestApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('pick/',views.pick, name='pick'),
    path('forms/',views.forms, name='forms'),
    path('cstud/',views.cstud, name='cstud'),
    path('fform/',views.fforms, name='fform'),
    path('cfac/',views.cfac, name='cfac'),
    path('pending/',views.pending, name='pending'),
    path('sapproval/',views.sapproval, name='sapproval'),
    path('fapproval/',views.fapproval, name='fapproval'),
    path('approved/',views.approved, name='approved'),
    path('declined/',views.declined, name='declined'),
    path('sinfo/',views.sinfo, name='sinfo'),
    path('finfo/',views.finfo, name='finfo'),
    path('registration/',views.newreg, name='newreg'),
   
  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
