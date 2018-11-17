from django.urls import path, include
from rest_framework import routers
from .views import LanguageView, ParadigmView, ProgrmmerView

router = routers.DefaultRouter()
router.register('languages', LanguageView)
router.register('paradigms', ParadigmView)
router.register('programmers', ProgrmmerView)

urlpatterns = [
    path('', include(router.urls))
]
