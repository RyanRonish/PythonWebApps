from django.urls import path, include
#from .views_accounts import UserAddView, UserUpdateView
from hero.views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/edit',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

]
