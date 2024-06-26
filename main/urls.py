from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IntroductionViewSet, AboutViewSet, ProjectViewSet, ResumeViewSet, ContactViewSet, BlogViewSet

router = DefaultRouter()
router.register(r'introductions', IntroductionViewSet)
router.register(r'abouts', AboutViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
