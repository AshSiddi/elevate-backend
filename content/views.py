from rest_framework import viewsets, permissions
from .models import Domain, Course, Announcement, Chapter, Subtopic, Flashcard, Question
from .serializers import DomainSerializer, CourseSerializer, AnnouncementSerializer, ChapterSerializer, SubtopicSerializer, FlashcardSerializer, QuestionSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

# Custom permission to allow read for authenticated users, write for admins only
class AdminWriteOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS for authenticated users
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # Allow POST, PUT, DELETE for admins only
        return request.user and (request.user.is_staff or request.user.is_superuser)

class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [AdminWriteOrReadOnly]  # Admin-only writes, authenticated reads

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AdminWriteOrReadOnly]

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [AdminWriteOrReadOnly]

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [AdminWriteOrReadOnly]

class SubtopicViewSet(viewsets.ModelViewSet):
    queryset = Subtopic.objects.all()
    serializer_class = SubtopicSerializer
    permission_classes = [AdminWriteOrReadOnly]

class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    permission_classes = [AdminWriteOrReadOnly]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AdminWriteOrReadOnly]