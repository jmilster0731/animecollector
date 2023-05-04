from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animes/', views.animes_index, name='animes_index'),
    path('animes/<int:anime_id>/', views.animes_detail, name='anime_detail'),
    path('animes/create/', views.Anime_Create.as_view(), name='anime_create'),
    path('animes/<int:pk>/update/', views.Anime_Update.as_view(), name='anime_update'),
    path('animes/<int:pk>/delete/', views.Anime_Delete.as_view(), name='anime_delete'),
    path('studios/create', views.Studio_Create.as_view(), name='studio_create'),
]
