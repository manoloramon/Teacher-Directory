from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.index, name='index'),
    path('<teacher_fname>', views.detail, name='detail')
]