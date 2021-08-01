from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path('movie/', views.WatchListAV.as_view()),
    path('movie/<int:pk>', views.WatchDetailAV.as_view()),

    path('', include(router.urls)),
    # path('stream/', views.StreamPlatFormAV.as_view()),
    # path('stream/<int:pk>', views.StreamPlatFormDetailAV.as_view()),

    path('stream/<int:pk>/review-create', views.ReviewCreate.as_view()),
    path('stream/<int:pk>/review', views.ReviewList.as_view()),
    path('stream/review/<int:pk>', views.ReviewDetail.as_view())
    # path('review/', views.ReviewList.as_view()),
    # path('review/<int:pk>/', views.ReviewDetail.as_view())
]