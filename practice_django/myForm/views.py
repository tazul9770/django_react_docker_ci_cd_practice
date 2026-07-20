from django.shortcuts import render, redirect
from myForm.forms import StudentsForm
from django.contrib import messages

def test_form(request):
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
            return redirect('test_form')
    return render(request, 'form/demoForm.html', {'form':form})
