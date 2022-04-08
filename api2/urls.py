from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api2.views import UserViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),     # api2/users/
]
