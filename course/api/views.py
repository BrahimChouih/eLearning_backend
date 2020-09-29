from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import *
from course.models import Course
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
        request.data['owner'] = request.user.id
        request.data['rate'] = 0.0
        request.data['numReviewers'] = 0
        return super().create(request, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        course = Course.objects.get(id=pk)
        if course.owner.id == request.user.id:
            return super().destroy(request, pk, *args, **kwargs)
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
        request.data['owner'] = request.user.id
        try:
            reter = Rater.objects.get(
                owner=request.data['owner'], rate_on=request.data['rate_on'])
            return Response({'response': 'you are rated this course before now'})
        except:
            return super().create(request, *args, **kwargs)

    def getRaterOnCourse(self, request, pk, *args, **kwargs):
        rater = Rater.objects.filter(rate_on=pk).values()

        return Response(rater)
