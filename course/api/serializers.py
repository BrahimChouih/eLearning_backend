from rest_framework import serializers
from course.models import Course, Video, Reviewer, Rater, Category


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        # exclude = ('create_at',)

    # def save(self):
    #     course = Course(
    #         title=self.validated_data['title'],
    #         description=self.validated_data['description'],
    #         owner=self.validated_data['owner'],
    #         cover=self.validated_data['cover'],
    #         price=self.validated_data['price'],
    #         rate=self.validated_data['rate'],
    #         numReviewers=self.validated_data['numReviewers'],
    #         category=self.validated_data['category'],
    #     )
    #     course.save()
    #     return course
