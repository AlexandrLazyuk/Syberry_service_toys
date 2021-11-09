from django.urls import path, include
from rest_framework import routers
from .views import GameViewSet, ToyViewSet


router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'toys', ToyViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]