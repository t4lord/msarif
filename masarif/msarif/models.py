from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Salary(models.Model):
    salary = models.IntegerField(verbose_name='الراتب')
    date = models.DateTimeField(editable=True, auto_now_add=True, verbose_name='التاريخ')
    date.editable=True
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.salary) + " ___ "+ str(self.date)