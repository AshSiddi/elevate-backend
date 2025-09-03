from django.db import models
from django.conf import settings
from content.models import Course  # Import from content app

class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='studying')  # e.g., 'studying', 'completed'
    enrolled_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user} - {self.course.name}"

class QuizAnalytics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_analytics')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_status = models.JSONField(default=dict)  # e.g., {"qid1": "correct", ...}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"Quiz Analytics for {self.user} - {self.course.name}"

class MockAnalytics(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mock_analytics')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_status = models.JSONField(default=dict)  # e.g., {"qid1": "correct", ...}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"Mock Analytics for {self.user} - {self.course.name}"