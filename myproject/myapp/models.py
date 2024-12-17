from django.db import models

# Create your models here.
class Course(models.Model):
    c_id = models.CharField(max_length= 50, unique=True)
    c_name = models.CharField(max_length=60)

    def __str__(self):
        return self.c_name