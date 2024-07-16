from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.IntegerField()
    City = models.TextField(max_length=50)

    def __str__(self):
        return self.Name+' '+self.Email
    class Meta:
        db_table = "Student"
        # managed = True
        # verbose_name = "Student"
        verbose_name_plural = "Student" 
        ordering=['-Name']

        