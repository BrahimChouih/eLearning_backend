from rest_framework import serializers
from accounts.models import Account
from course.models import Course


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'picture', 'country']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            picture=self.validated_data['picture'],
            country=self.validated_data['country']
        )

        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


class PurchasedCourses(serializers.ModelSerializer):
    owner = RegistrationSerializer(many=False)

    class Meta:
        model = Course
        # fields = '__all__'
        exclude = ('students',)


class AccountSerializer(serializers.ModelSerializer):
    purchased_courses = PurchasedCourses(many=True)

    class Meta:
        model = Account
        # fields = '__all__'
        exclude = ('password',)
