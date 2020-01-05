
from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import ProductViewSet,RatingViewSet,UserViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('rating', RatingViewSet)
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
