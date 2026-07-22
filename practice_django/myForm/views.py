from django.shortcuts import render, redirect
from myForm.forms import StudentsForm
from demo.models import Students
from django.contrib import messages

def create_student(request):
    form = StudentsForm()
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            #Normal form er jonno
            # name = form.cleaned_data.get('name')
            # roll = form.cleaned_data.get('roll')
            # address = form.cleaned_data.get('address')
            # courses = form.cleaned_data.get('course')
            # student = Students.objects.create(name=name, roll=roll, address=address)
            # student.courses.add(*courses)

            #model form er jonno
            student = form.save()
            courses = form.cleaned_data.get('courses')
            student.courses.add(*courses)
            messages.success(request, "Students added successfully")
            return redirect('create-student')
    return render(request, 'form/demoForm.html', {'form':form})

def update_student(request, id):
    student = Students.objects.prefetch_related('courses').get(id=id)
    #.prefetch_related('courese')
    form = StudentsForm(instance=student)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Students updated successfully")
            return redirect('update-student', id=student.id)
    return render(request, 'form/demoForm.html', {'form':form})

def delete_student(request, id):
    student = Students.objects.prefetch_related('courses').get(id=id)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect('stu-course')
    return render(request, 'stu_course.html')


