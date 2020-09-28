from django.urls import path
from .views import *
app_name = 'course'

urlpatterns = [
    path('courses/', courseList, name='All Courses'),
    path('courses/<int:courseId>/', getCourse, name='get a course'),
    path('courses/create/', createCourse, name='create a new course'),
    path('courses/update/<int:courseId>/',
         updateCourse, name='update a course'),
    path('courses/delete/<int:courseId>/',
         deleteCourse, name='delete a course'),
    path('rate/', rateCourse, name='rate on course'),

]
