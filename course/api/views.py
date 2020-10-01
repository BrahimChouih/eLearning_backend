from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from course.api.serializers import *
from course.models import Course, Rater, Reviewer, Video
from accounts.models import Account

############################ course API #####################


class CourseView(viewsets.ModelViewSet):

    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, ]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def create(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        request.data['rate'] = 0.0
        request.data['numReviewers'] = 0

        return super().create(request, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        course = Course.objects.get(id=pk)
        if course.owner.id == request.user.id:
            super().destroy(request, pk, *args, **kwargs)
            return Response({'response': 'Successfully delete this course'})
        else:
            return Response({'response': 'you don\'t have permission for this'})

    def partial_update(self, request, pk, *args, **kwargs):
        course = Course.objects.get(id=pk)
        if course.owner.id == request.user.id:
            return super().partial_update(request, pk, *args, **kwargs)
        else:
            return Response({'response': 'you don\'t have permission for this'})


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


class RaterView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer
    permission_classes = [IsAuthenticated, ]

    def rateCourse(self, request, *args, **kwargs):
        request.data['owner'] = request.user
        try:
            reter = Rater.objects.get(
                owner=request.data['owner'], rate_on=request.data['rate_on'])
            return Response({'response': 'you are rated this course before now'})
        except:
            return super().create(request, *args, **kwargs)

    def getRaterOnCourse(self, request, pk, *args, **kwargs):
        rater = Rater.objects.filter(rate_on=pk)
        serializer = RaterSerializer(rater, many=True)

        return Response(serializer.data)


class ReviewersView(viewsets.ModelViewSet):

    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            Reviewer.objects.get(
                owner=request.user,
                comment_on=request.data['comment_on'],
            )
            return Response({'response': 'your alrady writed a review on this course'})

        except:
            request.data['owner'] = request.user
            return super().create(request, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        try:
            Reviewer.objects.get(id=pk, owner=request.user)
            return super().partial_update(request, pk, *args, **kwargs)
        except:
            return Response({'response': 'you don\'t have permission for this'})

    def destroy(self, request, pk, *args, **kwargs):
        try:
            Reviewer.objects.get(id=pk, owner=request.user)
            super().destroy(request, pk, *args, **kwargs)
            return Response({'response': 'Successfully delete this Reviewer'})

        except:
            return Response({'response': 'you don\'t have permission'})


class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk, *args, **kwargs):
        try:
            course = Video.objects.get(id=pk).course
            Course.objects.get(id=course.id, owner=request.user)
            super().destroy(request, pk, *args, **kwargs)
            return Response({'response': 'Successfully delete this Reviewer'})

        except:
            return Response({'response': 'you don\'t have permission'})

    def getVidoes(self, request, pk):
        videos = Video.objects.filter(course=pk)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
