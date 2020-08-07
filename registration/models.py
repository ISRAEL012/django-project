from django.db import models

# Create your models here.
class Member(models.Model):
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    membership_date = models.DateField()

    def __str__(self):
        # Just return the attribute that attached to this method instead of the default string "Workshop object 1"
        # self is a python keyword => refers to the class "Student" itself
        # to access any field/attribute/property within the class itself (or outside the class):
        # self.field_name
        return (f"{self.firstname} {self.lastname}")  
