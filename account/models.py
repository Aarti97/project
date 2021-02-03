from django.db import models
from django.forms import ModelForm, Textarea

class Customer(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    cust_name= models.CharField(max_length=20, blank=True, null=True)
    phone_no = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=20, blank=True, null=True)

    

class Feedback(models.Model):
    name= models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=45, blank=True, null=True)
    message= models.TextField(max_length=100, blank=True, null=True)



class Meta:
    db_table = 'customer1'
    db_table ='feedback'
    
# Create your models here.
