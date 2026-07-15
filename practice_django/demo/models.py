from django.db import models

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Results(models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE, related_name='result')
    gpa = models.FloatField()
    passed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.name} - GPA: {self.gpa}"
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name