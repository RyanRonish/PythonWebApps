from django.urls import path, include
#from django.conf import settings
#from django.conf.urls.static import static
from hero.views import HeroCreateView, HeroDeleteView, HeroArticleView, HeroDetailView, HeroListView, HeroUpdateView, UserAddView, UserUpdateView
from hero.views import DocumentView
from django.contrib import admin

urlpatterns = [

    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/edit',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    path('article', HeroArticleView.as_view(), name='article_list'),

    #path('photo/add',                   PhotoCreateView.as_view(),  name='photo_add'),

    path('<str:doc>.md', DocumentView.as_view()),

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/<int:pk>',          UserUpdateView.as_view(),   name='account_edit'),
    path('accounts/signup/',            UserAddView.as_view(),      name='signup'),     

    path('admin/', admin.site.urls),     

]  

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
