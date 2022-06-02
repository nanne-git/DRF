from django.contrib import admin
from .models import Course, Teacher, ClassRoom, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(ClassRoom)
