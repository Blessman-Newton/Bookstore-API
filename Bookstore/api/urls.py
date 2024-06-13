from rest_framework import DefaultRouter
from django.urls import path, include
from .views import BookViewSet, OrderViewSet, ReviewViewSet


router = DefaultRouter()

router.register(r"books", BookViewSet)
router.register(r"order", OrderViewSet)
router.register(r"review", ReviewViewSet)


urlspattens = [
    path('', include(router.urls)),
]
