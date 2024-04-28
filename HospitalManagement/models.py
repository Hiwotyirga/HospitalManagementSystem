from django.db import models

# Create your models here.

class Userlogin (models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=50)


class Receptionlogin (models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=50)
