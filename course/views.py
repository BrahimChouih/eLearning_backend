from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action

from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.


@api_view(['GET', ])
@permission_classes((AllowAny,))
def apiOverview(request):

    api_overview = {
        "Authentication": "api/auth/ [login/register]",
        "COURSES": {
            'get all course': "api/courses/ [name='All Courses']",
            'get a course': "api/courses/<int:pk>/ [name='get a course']",
        },
        'RATE': {
            'rate on course': "api/rate/ [name='rate on course']",
            'get a rate': "api/rate/<int:pk>/",
        },
        'Comments': {
            'comment on course':	"api/reviewers/",
            'get a comment':	"api/reviewers/<int:pk>/",
        },
        'Videos': {
            'get all video': "api/videos/",
            'get a video': "api/videos/<int:pk>/",
        },
    }
    return Response(api_overview)