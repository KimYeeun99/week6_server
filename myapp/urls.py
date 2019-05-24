from django.urls import path,include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('',PostViewSet)
urlpatterns = [
    path('post/', include(routers.urls)),
]