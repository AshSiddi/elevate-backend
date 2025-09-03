from rest_framework import viewsets
from .models import HelpCenter, Blog, BlogReply, NewsletterSubscription, GeneralAnnouncement, HeroSection
from .serializers import (HelpCenterSerializer, BlogSerializer, BlogReplySerializer, 
                         NewsletterSubscriptionSerializer, GeneralAnnouncementSerializer, HeroSectionSerializer)
from .permissions import AllowReadOrAdminWrite, AllowCreateOrAdminWrite

class HelpCenterViewSet(viewsets.ModelViewSet):
    queryset = HelpCenter.objects.all()
    serializer_class = HelpCenterSerializer
    permission_classes = [AllowCreateOrAdminWrite]  # Authenticated read, public create, admin update/delete

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowReadOrAdminWrite]  # Public read, admin CRUD

class BlogReplyViewSet(viewsets.ModelViewSet):
    queryset = BlogReply.objects.all()
    serializer_class = BlogReplySerializer
    permission_classes = [AllowCreateOrAdminWrite]  # Authenticated read, public create, admin update/delete

class NewsletterSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
    permission_classes = [AllowCreateOrAdminWrite]  # Authenticated read, public create, admin update/delete

class GeneralAnnouncementViewSet(viewsets.ModelViewSet):
    queryset = GeneralAnnouncement.objects.all()
    serializer_class = GeneralAnnouncementSerializer
    permission_classes = [AllowReadOrAdminWrite]  # Public read, admin CRUD

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    permission_classes = [AllowReadOrAdminWrite]  # Public read, admin CRUD