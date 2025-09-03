from django.contrib import admin
from .models import Domain, Course, Announcement, Chapter, Subtopic, Flashcard, Question


# Register your models here.
admin.site.register([Domain, Course, Announcement, Chapter, Subtopic, Flashcard, Question])