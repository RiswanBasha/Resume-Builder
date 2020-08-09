from django.db import models

# Create your models here.

class Profile(models.Model):
    def __str__(self):
        return self.name
    


    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    summary=models.TextField(max_length=2000)
    degree=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    previous_work=models.TextField(max_length=2000)
    skills=models.TextField(max_length=2000)
    skills2=models.CharField(max_length=2000)
    skills3=models.CharField(max_length=2000)
    oskills=models.CharField(max_length=2000)
    achievements=models.TextField(max_length=2000)
    certify=models.TextField(max_length=2000)
    linkedin=models.CharField(max_length=2000)
    sgrade=models.CharField(max_length=2000)
    ugrade=models.CharField(max_length=2000)
    hobbies=models.TextField(max_length=2000)
    languages=models.TextField(max_length=2000)
    about=models.TextField(max_length=2000)
    projects=models.TextField(max_length=20000)
    branch=models.CharField(max_length=200)


