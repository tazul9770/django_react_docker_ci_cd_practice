from django.urls import path
from demo.views import test, check_template, user_dashboard, admin_dashboard

urlpatterns = [
    path('test/', test),
    path('check_template/', check_template),
    path('admin_dash/', admin_dashboard),
    path('user_dash/', user_dashboard)
]
