# uname = Srinivas & pwd = admin123

from django.contrib import admin
from TokenAuthentication_App.models import Emp

class EmpAdmin(admin.ModelAdmin):
    list_display = ['empid',
                    'empname',
                    'empsal',
                    'created',
                    'modified']

admin.site.register(Emp , EmpAdmin)