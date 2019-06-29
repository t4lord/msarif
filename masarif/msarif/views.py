from django.shortcuts import render, get_list_or_404
from .models import Salary
from .forms import NewSalaryForms
# Create your views here.

def main(request):
    obj = get_list_or_404(Salary)
    print(obj)
    context = {"title": "title", 'obj': obj}
    return render(request, "msarif/main.html", context)

def income(request):
    field_name = 'date'
    obj = Salary.objects.last()   
    field_object = Salary._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)
    salaryForm = NewSalaryForms(request.POST)
    if salaryForm.is_valid():
        salary = salaryForm.cleaned_data['salary']
        date = salaryForm.cleaned_data['date']
        yearForm = str(salary)[:4]
        monthForm = str(date)[5:7]
        # if date > field_value
        print(True)
            # salaryForm.save()


    context = {'title':'income', 'salaryForm': salaryForm}
    return render(request, "msarif/income.html", context)
