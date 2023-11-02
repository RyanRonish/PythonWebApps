from django.urls import path
from django.urls.conf import include
from superPhotos.views import PhotoDetailView, PhotoListView

urlpatterns = [
    path('', PhotoListView.as_view()),
    path('<int:id>', PhotoDetailView.as_view()),
]
