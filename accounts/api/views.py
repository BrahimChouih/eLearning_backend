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
        if(pk == 0):
            data = AccountSerializer(request.user, many=False)
        else:
            account = Account.objects.get(id=pk)
            data = AccountSerializer(account, many=False)
        return Response(data.data)

    def updateUserInfo(self, request, pk, *args, **kwargs):
        if(pk != request.user.id):
            return Response({'response': 'this is not your account'},status=400)

        usernames = []
        for i in Account.objects.all():
            usernames.append(i.username.lower())

        try:
            if(request.data['username'].lower() in usernames):
                return Response({"username": ["account with this username already exists."]},status=400)
        except:
            print('')

        return super().partial_update(request, pk, *args, **kwargs)
