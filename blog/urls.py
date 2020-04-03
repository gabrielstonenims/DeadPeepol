from django.urls import path

from . import views
from .views import GalleryView


urlpatterns = [
    path('',views.home,name='home'),
    path('albums/',views.album,name='albums'),
    path('album_tracks/<slug:slug>/',views.album_detail,name='album_track_detail'),
    path('album/<slug:slug>/',views.album_detail_afteremail,name='album_afteremail_detail'),
    path('candownload/',views.can_download,name='candownload'),
    path('can_download_track/<slug:slug>/',views.can_download_tracks,name='can_download_tracks_detail'),
    path('download_now/<slug:slug>/',views.download_now,name='download_now'),
    path('gallery/',GalleryView.as_view(),name='gallery'),
    path('about/',views.about,name='about'),
    path('events/',views.events,name='events')
]