from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),

    # Course create & update
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:course_id>/update/', views.course_update, name='course_update'),

    # Student create & update
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:student_id>/update/', views.student_update, name='student_update'),
]
