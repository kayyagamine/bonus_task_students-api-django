from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    course = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
