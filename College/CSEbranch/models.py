from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    student_id = models.IntegerField()

    def __str__(self):
        self.name