from rest_framework import serializers
from .models import UserCourse, QuizAnalytics, MockAnalytics

class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ['id', 'course', 'status', 'enrolled_at', 'updated_at']

class QuizAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnalytics
        fields = ['id', 'course', 'question_status', 'created_at', 'updated_at']

class MockAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockAnalytics
        fields = ['id', 'course', 'question_status', 'created_at', 'updated_at']