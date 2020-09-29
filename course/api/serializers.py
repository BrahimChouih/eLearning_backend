from rest_framework import serializers
from course.models import Course, Video, Reviewer, Rater, Category


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rater
        fields = ['owner', 'stars', 'rate_on', ]


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
