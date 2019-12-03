from django.db import models

# Create your models here.
class Student(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=15)
    age = models.IntegerField(default=15)
    Data_birth = models.DateTimeField()
    def __str__(self):
        return self.First_name

class Degree(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    student_Degree = models.IntegerField(default=15)



