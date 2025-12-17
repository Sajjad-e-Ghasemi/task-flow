from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', views.TaksView, basename='tasks')

urlpatterns = [
    path("", include(router.urls))
]
