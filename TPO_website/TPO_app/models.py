from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    uname = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=200)
    event = models.CharField(max_length=20)
    
    def __str__(self):
        return self.uname


class JobInfo(models.Model):
    uname = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=200)
    college = models.CharField(max_length=20)
    graduation = models.DecimalField(max_digits=19, decimal_places=2)
    company = models.CharField(max_length=200)
    profile = models.CharField(max_length=200)

    def __str__(self):
        return self.company
        
class EventInfo(models.Model):
    eventname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    eventdate = models.CharField(max_length=200)
    
    def __str__(self):
        return self.eventname

class CompanyInfo(models.Model):
    cname = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    
    def __str__(self):
        return self.cname

