from django.urls import path
from myForm.views import test_form


urlpatterns = [
    path('demoForm/', test_form, name='test_form')
]
