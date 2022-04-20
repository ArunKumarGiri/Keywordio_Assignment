from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    writter = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)