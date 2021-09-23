from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from .credentials import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from .utils import *

class AuthURL(APIView):
	def get(self, request, format=None):
		scopes = 'user-top-read'
		url = Request('GET', 'https://accounts.spotify.com/authorize', params={
				'client_id': CLIENT_ID,
				'response_type':'code',
				'redirect_uri': REDIRECT_URI,
				'scope': scopes
			}).prepare().url
		return redirect(url)

def spotifyCallback(request, format=None):
	code = request.GET.get('code')
	error = request.GET.get('error')

	response = post('https://accounts.spotify.com/api/token', data={
				'grant_type': 'authorization_code',
				'code': code,
				'redirect_uri': REDIRECT_URI,
				'client_id': CLIENT_ID,
				'client_secret': CLIENT_SECRET
			}).json()

	access_token = response.get('access_token')
	token_type = response.get('token_type')
	expires_in = response.get('expires_in')
	refresh_token = response.get('refresh_token')
	error = response.get('error')

	if not request.session.exists(request.session.session_key):
		request.session.create()

	updateOrCreateUserTokens(request.session.session_key, access_token, 
		token_type, expires_in, refresh_token)

	return redirect('frontend-main')

class IsSpotifyAuthenticated(APIView):
	def get(self, request, format=None):
		is_Authenticated = isAuthenticated(self.request.session.session_key)
		return Response({'status': is_Authenticated}, status=status.HTTP_200_OK)

# Spotify API Requests

class GetTopTracks(APIView):
	def get(self, request, term="medium_term", limit="50"):
		session_id = self.request.session.session_key
		endpoint = "top/tracks?time_range=" + term + "&limit=" + limit
		response = executeSpotifyApiRequest(session_id, endpoint)

		if 'error' in response or 'items' not in response:
			return Response({'error': "Could access top artists"}, 
					status=status.HTTP_204_NO_CONTENT)

		songsList = self.topTracksCleaned(response)

		return Response(songsList, status=status.HTTP_200_OK)

	def topTracksCleaned(self, jsonResponse):
		items = jsonResponse.get("items")
		songsList = {}
		count = 0
		for i in items:
			name = i.get("name")
			song_id = i.get("id")
			duration_ms = i.get("duration_ms")
			popularity = i.get("popularity")
			cover = i.get("album").get("images")[2].get("url")

			artist_string = ""

			for index, artist in enumerate(i.get("album").get("artists")):
				if index>0:
					artist_string += ", "
				artist_name = artist.get("name")
				artist_string += artist_name

			song = {
				'name': name,
				'song_id': song_id,
				'duration_ms': duration_ms,
				'popularity': popularity,
				'artists': artist_string,
				'image': cover
			}

			songsList[count] = song
			count += 1
			
		return songsList

class GetTopArtists(APIView):
	def get(self, request, term="medium_term", limit="50"):
		session_id = self.request.session.session_key
		endpoint = "top/artists?time_range=" + term + "&limit=" + limit
		response = executeSpotifyApiRequest(session_id, endpoint)

		if 'error' in response or 'items' not in response:
			return Response({"error: Could access top artists"}, status=status.HTTP_204_NO_CONTENT)

		artistList = self.topArtistsCleaned(response)
		return Response(artistList, status=status.HTTP_200_OK)

	def topArtistsCleaned(self, jsonResponse):
		items = jsonResponse.get("items")
		artistList = {}
		count = 0
		for i in items:
			name = i.get("name")
			artist_id = i.get("id")
			popularity = i.get("popularity")
			cover = i.get("images")[2].get("url")
			type_ = i.get("type")

			artist = {
				'name': name,
				'artist_id': artist_id,
				'popularity': popularity,
				'image': cover,
				'type': type_
			}

			artistList[count] = artist
			count += 1
			
		return artistList