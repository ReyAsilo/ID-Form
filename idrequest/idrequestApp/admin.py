from django.contrib import admin
from .models import studenttable, facultytable, registration
# Register your models here.

admin.site.register(studenttable)
admin.site.register(facultytable)
admin.site.register(registration)