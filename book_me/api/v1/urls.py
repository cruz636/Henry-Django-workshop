
from django.urls import path, include
from book_me.api.v1.viewsets import *
from rest_framework.routers import DefaultRouter

from book_me.api.v1.viewsets import *

router = DefaultRouter()
router.register("eventos", EventosViewSet)
router.register("artistas", ArtistasViewSet)


urlpatterns = [
    path("", include(router.urls)),
]