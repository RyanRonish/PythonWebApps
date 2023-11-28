from django.urls import path
from hero.views import HeroListView, HeroDetailView

urlpatterns = [
    path('', HeroListView.as_view()),
    path('<str:id>', HeroDetailView.as_view()),
]
