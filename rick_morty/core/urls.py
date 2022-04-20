from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("character/<int:pk>", views.CharacterDetail.as_view(), name='character-detail'),
    path("episodes/", views.EpisodeIndex.as_view(), name='episode-index'),
    path("episodes/<int:pk>", views.EpisodeDetail.as_view(), name='episode-detail'),
    path("<int:pk>", views.Index.as_view(), name='index'),
    path("register", views.CreateUserView.as_view(), name='register'),
    path("register_success", views.RegisterSuccessView.as_view(), name='register_success')

]