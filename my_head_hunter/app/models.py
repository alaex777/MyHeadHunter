from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Worker(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    contacts = models.CharField(max_length=256, blank=True)

class WorkExperience(models.Model):
    user = models.OneToOneField(Worker, on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Employer(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    amount_of_employees = models.IntegerField(blank=True)
    address = models.CharField(max_length=128, blank=True)
    contacts = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)

class Vacancy(models.Model):
    employer = models.OneToOneField(Employer, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    salary = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)

class Message(models.Model):
    employer = models.OneToOneField(Employer, on_delete=models.CASCADE)
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    message = models.TextField()
