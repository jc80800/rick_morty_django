from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("character/<int:pk>", views.CharacterDetail.as_view(), name='character-detail'),
    path("episodes/", views.EpisodeIndex.as_view(), name='episode-index'),
    path("<int:pk>", views.Index.as_view(), name='index')
]