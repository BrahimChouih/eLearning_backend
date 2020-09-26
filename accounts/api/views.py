from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.api.serializers import RegistrationSerializer


@api_view(['POST', ])
@permission_classes((AllowAny,))
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if request.method == 'POST':
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully registrated a new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['purchased_courses'] = []

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    return Response(serializer.data)


def getUserInfo(request):
    data = {}
    data['id'] = request.user.id
    data['email'] = request.user.email
    data['username'] = request.user.username
    data['country'] = request.user.country

    data['purchased_courses'] = request.user.purchased_courses.all().values()

    try:
        data['picture'] = request.user.picture.url
    except:
        data['picture'] = None

    return data


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def userInfo(request):
    data = getUserInfo(request)

    return Response(data)
