from django.urls import path, include

from .views_accounts import UserAddView, UserUpdateView
from .views_hero import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView
from django.contrib import admin

urlpatterns = [

    # Hero
    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),


    # Admin views for users
    # path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]