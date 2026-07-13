from django.shortcuts import render
from django.http import HttpResponse
from demo.models import Student, Results
from django.db.models import Avg, Max, Min

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

def student_results_view(request):
    students = Student.objects.select_related('result').all()
    high_gpa_students = Student.objects.filter(result__gpa__gte = 3.5)
    low_gpa_students = Student.objects.filter(result__gpa__lt = 3.5) 
    pass_students = Student.objects.filter(result__passed = True)
    stats = Results.objects.aggregate(
        avg_gpa = Avg("gpa"),
        max_gpa = Max("gpa"),
        min_gpa = Min("gpa")
    )
    good_students = Student.objects.filter(result__passed=True, result__gpa__gte=3.0)
    context = {
        "students":students,
        "high_gpa_students":high_gpa_students,
        "low_gpa_students":low_gpa_students,
        "pass_students":pass_students,
        "stats":stats,
        "good_students":good_students
    }
    return render(request, 'student.html', context)
