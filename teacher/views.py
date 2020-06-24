from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Teacher

# Create your views here.
def index(request): 
    # SELECT * FROM teacher_teacher
    # output = ', '.join([t.firstName for t in teacher])
    # SELECT * FROM teacher_teacher WHRE firstName = 'Anna'
    # Teacher.objects.filter(firstName='Anna')
    # Teacher.objects.get('id=1')
    # return HttpResponse(output)

    teacher = Teacher.objects.all()
    return render(request, 'teacher/index.html', {'teacher': teacher})

def detail(request, teacher_fname):
    teacher = get_object_or_404(Teacher, firstName = teacher_fname)
    return render(request, 'teacher/detail.html', {'teacher': teacher})
    