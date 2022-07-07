# spotify - urls.py 
from django.urls import path
from .views import *

urlpatterns = [
    path('get-auth-url', AuthURL.as_view(), name="spotify-auth"),
    path('redirect', spotifyCallback, name="spotify-callback"),
    path('is-authenticated', IsSpotifyAuthenticated.as_view(), name="is-spotify-auth"),
    path('top-tracks', GetTopTracks.as_view(), name="top-tracks"),
    path('top-artists', GetTopArtists.as_view(), name="top-artists"),
    path('top-tracks/<str:term>/<str:limit>', GetTopTracks.as_view()),
    path('top-artists/<str:term>/<str:limit>', GetTopArtists.as_view())
]