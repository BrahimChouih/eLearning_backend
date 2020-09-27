from django.urls import path
from .views import *
app_name = 'course'

urlpatterns = [
    path('courses/', courseList, name='All Courses'),
    path('courses/<int:courseId>/', getCourse, name='get a course'),
    path('courses/create/', createCourse, name='create a new course'),
]
