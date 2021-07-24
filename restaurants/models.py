from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

    #For Printing
    def __str__(self):
        return self.first_name + ' ' +  self.last_name

class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    #For Printing
    def __str__(self):
        return self.name
