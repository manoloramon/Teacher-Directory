from django.db import models
from tastypie.resources import ModelResource
from teacher.models import Teacher


class TeacherResource(ModelResource):
    class Meta:
        queryset = Teacher.objects.all()
        resource_name = 'teacher'
        excludes = ['date_created']
