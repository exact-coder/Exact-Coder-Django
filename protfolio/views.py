from django.shortcuts import render
from protfolio.models import OurWork,Quote
from home.models import BreadCrumb
from accounts.models import Employee
from django.core.paginator import Paginator

# Create your views here.

def protfolio(request):
    result = OurWork.objects.prefetch_related().order_by('-pkid')
    bread_crumb = BreadCrumb.objects.filter(page_type="PROTFOLIO",type_check="SHOW").first()
    paginate_result = Paginator(result,8,orphans=3)
    page_number = request.GET.get('page')
    ourworks = paginate_result.get_page(page_number)
    context = {
        "ourworks" : ourworks,
        'bread_crumb':bread_crumb,
    }
    return render(request, 'pages/protfolio.html',context)

def ourWorkDetails(request,id,slug):
    workdetails = OurWork.objects.get(id=id,slug=slug)
    context = {
        "ourWorkDetails":workdetails,
    }
    return render(request,'pages/workdetails.html',context)

def exactCoders(request):
    quotes = Quote.objects.prefetch_related()
    employee_obj = Employee.objects.prefetch_related()
    bread_crumb = BreadCrumb.objects.filter(page_type="EXACTCODERS",type_check="SHOW").first()
    employee_paginator = Paginator(employee_obj,9,orphans=4)
    page_number = request.GET.get('page')
    employees = employee_paginator.get_page(page_number)
    context ={
        'employees' : employees,
        'quotes': quotes,
        'bread_crumb':bread_crumb,
    }
    return render(request, 'pages/exactCoders.html',context)

