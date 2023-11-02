
from django.contrib import admin
from django.urls import path
from django.contrib.admin import site
from hero.views import HeroListView, HeroDetailView

urlpatterns = [
    path(r'admin/', site.urls),
    path('', HeroListView.as_view()),
    path('<str:id>', HeroDetailView.as_view()),
]
