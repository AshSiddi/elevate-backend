from rest_framework import serializers
from .models import Domain, Course, Announcement, Chapter, Subtopic, Flashcard, Question

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'name', 'created_at', 'updated_at']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'domain', 'name', 'about_primary', 'about_secondary', 'total_questions', 'total_chapters', 'created_at', 'updated_at']

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'course', 'primary_text', 'secondary_text', 'created_at']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'course', 'name', 'created_at', 'updated_at']

class SubtopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtopic
        fields = ['id', 'chapter', 'name', 'created_at', 'updated_at']

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ['id', 'subtopic', 'primary_text', 'secondary_text', 'created_at', 'updated_at']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'subtopic', 'text', 'option0', 'option1', 'option2', 'option3', 'correct_option', 'explanation', 'created_at', 'updated_at']