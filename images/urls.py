from django.urls import path
from .views import ImageViewSet, RetrieveImage

urlpatterns = [
    path('upload/', ImageViewSet.as_view(), name='upload'),
    path('retrieve/', RetrieveImage.as_view()),
]