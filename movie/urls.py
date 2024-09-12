from django.urls import path,include
from .views import  MovieViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',MovieViewSet,basename='')

urlpatterns=[
    path('docs/',include_docs_urls(title="Movie Docs"))
]

urlpatterns+= router.urls