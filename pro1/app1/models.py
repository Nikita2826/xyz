from django.db import models

# Create your models here.
class Person(models.Model):
    Pid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    City = models.CharField(max_length=40)
    Birth_date = models.DateField()
    Adhar_no = models.IntegerField()
    Pancard_no = models.CharField(max_length=30)

