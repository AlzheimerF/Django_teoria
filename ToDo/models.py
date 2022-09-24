from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ToDo(models.Model):
    name = models.CharField(max_length=250)
    exercise = models.TextField()

    def __str__(self):
        return self.name