from django import forms
from .models import Salary
import datetime
class NewSalaryForms(forms.Form):
    salary = forms.IntegerField()
    date = forms.DateField(widget=forms.SelectDateWidget)
    