from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet
from events.views import EventViewSet  # ⬅️ Import EventViewSet
from content.views import DomainViewSet, CourseViewSet, AnnouncementViewSet, ChapterViewSet, SubtopicViewSet, FlashcardViewSet, QuestionViewSet
from user_extras.views import FavoriteViewSet, NotificationViewSet, ChatMessageViewSet
from user_progress.views import UserCourseViewSet, QuizAnalyticsViewSet, MockAnalyticsViewSet
from platform_specifics.views import HelpCenterViewSet, BlogViewSet, BlogReplyViewSet, NewsletterSubscriptionViewSet, GeneralAnnouncementViewSet, HeroSectionViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'events', EventViewSet, basename='event')  # ⬅️ Register EventViewSet

# Content Routes (admin-only CRUD, authenticated read)
router.register(r'domains', DomainViewSet, basename='domain')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'chapters', ChapterViewSet, basename='chapter')
router.register(r'subtopics', SubtopicViewSet, basename='subtopic')
router.register(r'flashcards', FlashcardViewSet, basename='flashcard')
router.register(r'questions', QuestionViewSet, basename='question')

# User Extras Routes (user-specific)
router.register(r'favorites', FavoriteViewSet, basename='favorite')  # Added basename
router.register(r'notifications', NotificationViewSet, basename='notification')  # Added basename
router.register(r'chat_messages', ChatMessageViewSet, basename='chat_message')  # Added basename

# Progress Routes (user-specific)
router.register(r'user_courses', UserCourseViewSet, basename='user_course')  # Added basename
router.register(r'quiz_analytics', QuizAnalyticsViewSet, basename='quiz_analytic')  # Added basename
router.register(r'mock_analytics', MockAnalyticsViewSet, basename='mock_analytic')  # Added basename

# Platform Routes (public access)
router.register(r'help_center', HelpCenterViewSet, basename='help_center')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'blog_replies', BlogReplyViewSet, basename='blog_reply')
router.register(r'newsletter_subscriptions', NewsletterSubscriptionViewSet, basename='newsletter_subscription')
router.register(r'general_announcements', GeneralAnnouncementViewSet, basename='general_announcement')
router.register(r'hero_sections', HeroSectionViewSet, basename='hero_section')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
