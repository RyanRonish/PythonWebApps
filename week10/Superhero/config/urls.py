from django.urls import path, include
from hero.views import HeroCreateView, HeroDeleteView, HeroArticleView, HeroDetailView, HeroListView, HeroUpdateView, UserAddView, UserUpdateView
from hero.views import DocumentView, HeroArticleUpdateView
from django.contrib import admin

urlpatterns = [

    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/edit',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    path('article', HeroArticleView.as_view(), name='article_list'),
    path('<int:pk>/article_edit',  HeroArticleUpdateView.as_view(),  name='article_edit'),

    path('<str:doc>.md', DocumentView.as_view()),

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>',          UserUpdateView.as_view(),   name='account_edit'),
    path('accounts/signup/',            UserAddView.as_view(),      name='signup'),     

    path('admin/', admin.site.urls),     

]
