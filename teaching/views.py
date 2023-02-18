from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Group, Student, Mark, CenterInfo


def index(request):
    academy = CenterInfo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        group_id = request.POST.get('group_id')
        student = Student.objects.create(name=name, last_name=last_name, phone_number=phone_number, group_id=group_id)
    edu_groups = Group.objects.all()
    edu_students = Student.objects.all()

    contex = {'groups': edu_groups, 'students': edu_students, 'academy': academy}

    return render(request, 'index.html', context=contex)


def group(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        students = Student.objects.filter(group_id=group_id)
        context = {'groups': groups, 'students': students}

        return render(request, 'group.html', context=context)

    context = {'groups': groups}

    return render(request, 'group.html', context=context)


def mark(request):
    students = Student.objects.all()
    marks = Mark.objects.all()
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        mark = request.POST.get('mark')
        student_marks = Mark.objects.create(student_id=student_id, mark=mark)
        marks = Mark.objects.all()
        students = Student.objects.all()

        context = {'marks': marks, 'students': students}
        return render(request, 'mark.html', context=context)

    context = {'students': students, "marks": marks}
    return render(request, 'mark.html', context=context)


def centerinfo(request):
    centerinfo = CenterInfo.objects.all()
    if request.method == "POST":
        centerinfo = request.POST.get('centerinfo')
    
    context = {'centerinfo': centerinfo,}
    return render(request, 'centerinfo.html', context=context)

def academy(request):
 
    print(context)
    
    return render(request, 'index.html', context=context)

    
    
    





