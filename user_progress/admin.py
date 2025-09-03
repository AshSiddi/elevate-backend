from django.contrib import admin
from .models import UserCourse, QuizAnalytics, MockAnalytics

# Register your models here.
admin.site.register([UserCourse, QuizAnalytics, MockAnalytics])