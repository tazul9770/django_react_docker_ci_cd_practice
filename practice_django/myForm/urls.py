from django.urls import path
from myForm.views import create_student, update_student, delete_student


urlpatterns = [
    path('create_student/', create_student, name='create-student'),
    path('update_student/<int:id>/', update_student, name='update-student'),
    path('delete_student/<int:id>/', delete_student, name='delete-student')
]
