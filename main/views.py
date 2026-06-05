from django.shortcuts import render
from .models import Course, Student


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
