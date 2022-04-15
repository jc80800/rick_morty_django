from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name='index'),
    path("character/<int:pk>", views.CharacterDetail.as_view(), name='character-detail')
]