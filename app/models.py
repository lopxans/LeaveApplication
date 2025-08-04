from django.db import models

# Create your models here.
class Student(models.Model):
    roll_number = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)
    student_contact = models.CharField(max_length=15)
    student_email = models.EmailField()
    
    is_delete = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(null=True)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    message = models.TextField(null=True, blank=True)
    
    is_delete = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(null=True)