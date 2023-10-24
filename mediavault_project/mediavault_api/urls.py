from django.urls import path
from . import views

urlpatterns = [
    path('bands/', views.BandList.as_view()),
    path('band/<int:pk>/', views.BandDetail.as_view()),
    path('songs/', views.SongList.as_view()),
    path('song/<int:pk>/', views.SongDetail.as_view()),
    path('albums/', views.AlbumList.as_view()),
    path('album/<int:pk>/', views.AlbumDetail.as_view()),
    path('albumreviews/', views.AlbumReviewList.as_view()),
    path('albumreview/<int:pk>/', views.AlbumReviewDetail.as_view()),
]
