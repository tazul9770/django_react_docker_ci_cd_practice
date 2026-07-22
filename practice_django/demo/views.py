from django.shortcuts import render
from django.http import HttpResponse
from demo.models import Student, Results, Category, Product, Students, Course
from django.db.models import Avg, Max, Min, Count, Q

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

def product_view_list(request):
    product = Product.objects.select_related('category').all()
    category = Category.objects.prefetch_related('products').all()
    cheap_products = Product.objects.select_related('category').filter(price__lt=50)
    product_stats = Product.objects.aggregate(
        avg_price = Avg('price'),
        min_price = Min('price'),
        max_price = Max('price'),
        total_products = Count('id')
    )
    search_products = Product.objects.filter(
        Q(name__icontains='golap') | Q(description__icontains='bal')
    )
    context = {
        "product":product,
        "category":category,
        "cheap_products": cheap_products,
        "product_stats":product_stats,
        "search_products":search_products
    }
    
    return render(request, 'product/product.html', context)

def student_course_view(request):
    students = Students.objects.prefetch_related('courses').all()
    # stu_courses = Students.objects.get(name="Jamil").courses.all()
    course_students = Course.objects.get(title="Data Science").student.all()
    course_student_count = Course.objects.annotate(total_students=Count("student"))
    multi_course_students = Students.objects.annotate(num_courses=Count("courses")).filter(num_courses__gt=1)
    search_courses = Course.objects.filter(
        Q(title__icontains="Data") | Q(student__name__icontains="Jamil")
    ).distinct()
    context = {
        "students":students,
        # "stu_courses":stu_courses,
        "course_students":course_students,
        "course_student_count":course_student_count,
        "multi_course_students":multi_course_students,
        "search_courses":search_courses
    }
    return render(request, 'stu_course.html', context)