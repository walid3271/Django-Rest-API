from django.db import models

# Create your models here.
class user_model(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)