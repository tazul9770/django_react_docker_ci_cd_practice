from django.urls import path
from demo.views import test, check_template, user_dashboard, admin_dashboard, context_test, student_results_view, product_view_list, student_course_view

urlpatterns = [
    path('test/', test),
    path('check_template/', check_template),
    path('admin_dash/', admin_dashboard),
    path('user_dash/', user_dashboard),
    path('context/', context_test),
    path('student/', student_results_view),
    path('product/', product_view_list),
    path('stu_course/', student_course_view, name='stu-course')
]
