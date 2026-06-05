from django.shortcuts import render, redirect
from .models import Course, Student
from .forms import CourseForm, StudentForm


def index(request):
    courses = Course.objects.all()
    students = Student.objects.select_related('course').all()
    context = {
        'courses': courses,
        'students': students,
    }
    return render(request, 'main/index.html', context)


def course_students(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    context = {
        'course': course,
        'students': students,
    }
    return render(request, 'main/course_students.html', context)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'main/detail.html', context)


# --- Course Create & Update ---

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'main/course_form.html', {'form': form, 'action': 'Yaratish'})


def course_update(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_students', course_id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'main/course_form.html', {'form': form, 'action': 'Tahrirlash'})


# --- Student Create & Update ---

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'main/student_form.html', {'form': form, 'action': 'Yaratish'})


def student_update(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'main/student_form.html', {'form': form, 'action': 'Tahrirlash'})
