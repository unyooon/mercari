from importlib.resources import path
from rest_framework import routers
from django.urls import path 
from django.conf.urls import include

from .views import ProductViewSet

router = routers.SimpleRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
  path('', include(router.urls))
]