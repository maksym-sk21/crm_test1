from django.contrib import admin
from .models import StudentCalculation, School, Salary, TeacherCalculation, Turnover

# Register your models here.
admin.site.register(StudentCalculation)
admin.site.register(School)
admin.site.register(Salary)
admin.site.register(TeacherCalculation)
admin.site.register(Turnover)
