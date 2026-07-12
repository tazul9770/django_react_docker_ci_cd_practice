from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("This is test views")

def check_template(request):
    return render(request, "index.html")

def user_dashboard(request):
    return render(request, 'inheritance/user_dashboard.html')

def admin_dashboard(request):
    return render(request, 'inheritance/admin_dashboard.html')

def context_test(request):
    context = {
        "name":"Tazul Islam",
        "age": "25",
        "sex":"male"
    }
    return render(request, 'context.html', context)