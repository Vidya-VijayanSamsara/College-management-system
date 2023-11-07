from django.contrib import admin
from application.models import Admin,Login,Staff,Student
# Register your models here.
admin.site.register(Admin)
admin.site.register(Login)
admin.site.register(Staff)
admin.site.register(Student)