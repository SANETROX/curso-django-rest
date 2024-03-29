from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserProfileFeeItemViewSet)

urlpatterns = [
    path('hello-api/',  views.HelloApi.as_view(), name='hello api'),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]