from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CourseSerializer
from course.models import Course
from accounts.models import Account


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
        request.data['owner'] = request.user
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
            # print(serializer.data['cover'].url)

            return Response({
                'response': 'failed create a new course',
                'course': serializer.data['title']
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
