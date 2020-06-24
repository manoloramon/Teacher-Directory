from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'emailAddress', 'subjectsTaught')
    exclude = ('date_created', )
    
admin.site.register(Teacher, TeacherAdmin)