from django.shortcuts import render, get_list_or_404
from .models import Salary
# Create your views here.

def main(request):
    obj = get_list_or_404(Salary)
    print(obj)
    context = {"title": "title", 'obj': obj}
    return render(request, "msarif/main.html", context)

def income(request):
    return render(request, "msarif/income.html", {})