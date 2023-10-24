from django.urls import path
from . import views

urlpatterns = [
    path('bands/', views.BandList.as_view())
]
