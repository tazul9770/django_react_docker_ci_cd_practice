from django.contrib import admin
from django.urls import path
from demo.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', test)
]
