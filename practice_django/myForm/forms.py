from django import forms
from demo.models import Course, Students

# Django normal form
# class StudentsForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     roll = forms.IntegerField()
#     address = forms.CharField(max_length=200)
#     course = forms.ModelMultipleChoiceField(
#         queryset=Course.objects.all(),
#         widget=forms.SelectMultiple  
#     )

#Django model form
class StudentsForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.SelectMultiple,
        required=False 
    )
    class Meta:
        model = Students
        fields = ['name', 'roll', 'address', 'courses']