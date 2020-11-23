from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from accounts.api.serializers import RegistrationSerializer, AccountSerializer, AccountSerializer2, PurchasedCourses
from accounts.models import Account


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
            data['course_made_by_me'] = []

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
    return Response(serializer.data)


class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AccountSerializer2
        return AccountSerializer

    def userInfo(self, request, pk):
        # account = Account.objects.get(id=request.user.id)
        data = AccountSerializer(request.user, many=False)
        return Response(data.data)

    def updateUserInfo(self, request, pk, *args, **kwargs):
        if(pk != request.user.id):
            return Response({'response': 'this is not your account'})
        return super().partial_update(request, pk, *args, **kwargs)
