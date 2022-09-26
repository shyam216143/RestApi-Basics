from django.contrib import admin
from .models import employee,student
# Register your models here.
admin.site.register(employee)
admin.site.register(student)



# @admin.register(student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display: ['id','name,'age','roll', 'address']