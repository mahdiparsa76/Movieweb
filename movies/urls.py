from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_details/<slug:slug>', views.movie_details, name='movie_details'),
    path('actor_info/<slug:slug>', views.actor_details, name='actor_info'),
    path('genre/<slug:genere>', views.genre, name='genre'),
    path('search/', views.search, name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)