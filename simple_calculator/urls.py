CONTENT:
from django.contrib import admin
from django.urls import path
from calculator.views import home, calculate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('calculate/', calculate, name='calculate'),
]