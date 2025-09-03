from rest_framework import viewsets, permissions
from .models import UserCourse, QuizAnalytics, MockAnalytics
from .serializers import UserCourseSerializer, QuizAnalyticsSerializer, MockAnalyticsSerializer

class UserCourseViewSet(viewsets.ModelViewSet):
    serializer_class = UserCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QuizAnalyticsViewSet(viewsets.ModelViewSet):
    serializer_class = QuizAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return QuizAnalytics.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MockAnalyticsViewSet(viewsets.ModelViewSet):
    serializer_class = MockAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MockAnalytics.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)