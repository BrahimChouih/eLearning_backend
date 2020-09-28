from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import *
from course.models import Course
from accounts.models import Account

############################ course API #####################


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def courseList(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def getCourse(request, courseId):
    try:
        course = Course.objects.get(id=courseId)
        serializer = CourseSerializer(course, many=False)
        return Response(serializer.data)
    except:
        return Response({'error': 'this is course in not existe'})


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def createCourse(request):
    if request.method == 'POST':
        request.data['owner'] = request.user.id
        request.data['rate'] = 0.0
        request.data['numReviewers'] = 0
        serializer = CourseSerializer(data=request.data)

        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()

            return Response({
                'response': 'Successfully create a new course',
                'course': serializer.data
            })
        else:
            print(serializer.errors)
            print(serializer.data)
            return Response({
                'response': 'failed create a new course',
                'course': serializer.data['title']
            })


@ api_view(['PUT', ],)
@ permission_classes((IsAuthenticated,))
def updateCourse(requset, courseId):
    if requset.method == 'PUT':
        course = Course.objects.get(id=courseId)
        if requset.user != course.owner:
            return Response({'response': 'you don\'t have permission'})
        serializer = CourseSerializer(instance=course, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'response': 'updated successfully',
                'course': serializer.data,
            })
        else:
            return Response({
                'response': 'updated failed',
            })


@ api_view(['DELETE', ],)
@ permission_classes((IsAuthenticated,))
def deleteCourse(requset, courseId):
    if requset.method == 'DELETE':
        course = Course.objects.get(id=courseId)
        if requset.user != course.owner:
            return Response({'response': 'you don\'t have permission'})
        course.delete()
        return Response({
            'response': 'This Course is deleted',
        })


# {
#     "id": 2,
#     "title": "Django Course",
#     "description": "django django django django django django django",
#     "create_at": "2020-09-26T11:05:54.933915Z",
#     "cover": "/media/categories/None_xwvTuRE.png",
#     "price": 10000.0,
#     "rate": 0.0,
#     "numReviewers": 0,
#     "owner": 1,
#     "category": 3,
#     "students": [
#         2
#     ]
# }


######################### Rate API ################


@ api_view(['POST', ])
@ permission_classes((IsAuthenticated,))
def rateCourse(request):
    if request.method == 'POST':
        request.data['owner'] = request.user.id

        serializer = RaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'response': 'Successfully rate on this course',
                'rate': serializer.data
            })
        else:
            return Response({
                'response': 'failed rate on this course',
                'rate': serializer.data
            })
