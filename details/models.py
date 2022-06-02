from django.db import models


# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.course_name}"


class ClassRoom(models.Model):
    section = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.section}"


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return f"{self.name}"
