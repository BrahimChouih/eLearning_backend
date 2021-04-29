from django.urls import path
from .views import *
app_name = 'course'

urlpatterns = [
    ############## course API #####################
    path('courses/',
         CourseView.as_view({
             'get': 'list',
             'post': 'create',
         }), name='All Courses'),
    path('courses/<int:pk>/',
         CourseView.as_view({
             'get': 'retrieve',
             'put': 'partial_update',
             'delete': 'destroy',
         }), name='get a course'),
    path('coursesMadeByUser/<int:pk>/',
         CourseView.as_view({
             'get': 'coursesMadeByUser',
         }), name='coursesMadeByUser'),
    #################### rate API ########################
    path(
        'rate/', RaterView.as_view({
            'post': 'rateCourse',
            'get': 'list',
        }), name='rate on course'),
    path(
        'rate/<int:pk>/', RaterView.as_view({
            'get': 'getRaterOnCourse',
        })
    ),
    #################### reviewer API ########################

    path(
        'reviewers/', ReviewersView.as_view({
            'get': 'list',
            'post': 'create',
        })
    ),
    path(
        'reviewers/<int:pk>/', ReviewersView.as_view({
            'put': 'partial_update',
            'delete': 'destroy',
        })
    ),

    #################### Video API ########################
    path(
        'videos/', VideoView.as_view({
            'post': 'create',
        })
    ),

    path(
        'videos/<int:pk>/', VideoView.as_view({
            'get': 'getVidoes',
            'delete': 'destroy',
        })
    ),
]
