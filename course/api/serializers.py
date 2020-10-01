from rest_framework import serializers
from course.models import Course, Video, Reviewer, Category, Rater
from accounts.api.serializers import RegistrationSerializer, PurchasedCourses
from accounts.models import Account


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    owner = RegistrationSerializer(many=False, read_only=True, required=False)
    category = CategorySerializer(many=False, read_only=True)
    students = RegistrationSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, *args, **kwargs):
        owner = Account.objects.get(
            id=self.context['request'].data['owner'].id)
        category = Category.objects.get(
            id=self.context['request'].data['category'])
        course = Course.objects.create(
            title=self.validated_data['title'],
            description=self.validated_data['description'],
            cover=self.validated_data['cover'],
            price=self.validated_data['price'],
            rate=self.validated_data['rate'],
            numReviewers=self.validated_data['numReviewers'],
            owner=owner,
            category=category,
        )
        course.save()
        return course


class RaterSerializer(serializers.ModelSerializer):
    owner = RegistrationSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = Rater
        fields = '__all__'

    def create(self, *args, **kwargs):
        owner = Account.objects.get(
            id=self.context['request'].data['owner'].id)

        rater = Rater(
            owner=owner,
            stars=self.validated_data['stars'],
            rate_on=self.validated_data['rate_on'],
        )
        rater.save()
        return rater


class VideoSerializer(serializers.ModelSerializer):
    course = PurchasedCourses(many=False, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

    def create(self, *args, **kwargs):
        course = Course.objects.get(
            id=self.context['request'].data['course'])

        print(self.context['request'].data)

        video = Video(
            title=self.validated_data['title'],
            video=self.validated_data['video'],
            thumbnail=self.validated_data['thumbnail'],
            lessonNum=self.validated_data['lessonNum'],
            course=course,
        )
        video.save()
        return video


class ReviewerSerializer(serializers.ModelSerializer):
    owner = RegistrationSerializer(many=False, read_only=True, required=False)
    comment_on = CourseSerializer(many=False, read_only=True, required=False)
    rate = RaterSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = Reviewer
        fields = '__all__'

    def create(self, *args, **kwargs):
        owner = Account.objects.get(
            id=self.context['request'].data['owner'].id)

        comment_on = Course.objects.get(
            id=self.context['request'].data['comment_on'])

        reviewer = Reviewer(
            owner=owner,
            comment=self.validated_data['comment'],
            comment_on=comment_on,
        )
        reviewer.save()
        return reviewer
