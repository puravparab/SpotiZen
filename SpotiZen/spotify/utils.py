from django.utils import timezone
from datetime import timedelta
from .models import SpotifyToken
from .credentials import CLIENT_ID, CLIENT_SECRET
from requests import post, put, get

BASE_URL = "https://api.spotify.com/v1/me/"

def getUserToken(session_id):
	user_token = SpotifyToken.objects.filter(user=session_id)
	if user_token.exists():
		return user_token[0]
	else:
		return None

def isAuthenticated(session_id):
	tokens = getUserToken(session_id)
	if tokens:
		expiry = tokens.expires_in
		if (expiry <= timezone.now()):
			refreshSpotifyToken(session_id)
		return True
	else:
		return False

def updateOrCreateUserTokens(session_id, access_token, 
	token_type, expires_in, refresh_token):
	token = getUserToken(session_id)
	expires_in = timezone.now() + timedelta(seconds=expires_in)

	if token:
		token.access_token = access_token
		token.token_type = token_type
		token.expires_in = expires_in
		token.refresh_token = refresh_token
		token.save(update_fields=['access_token', 'token_type', 
			'expires_in', 'refresh_token'])

	else:
		token = SpotifyToken(
			user = session_id,
			access_token = access_token,
			token_type = token_type,
			expires_in = expires_in,
			refresh_token = refresh_token)
		token.save()

def refreshSpotifyToken(session_id):
	refresh_token = getUserToken(session_id).refresh_token

	response = post('https://accounts.spotify.com/api/token', data={
			'grant_type': 'refresh_token',
			'refresh_token': refresh_token,
			'client_id': CLIENT_ID,
			'client_secret': CLIENT_SECRET
		}).json()

	access_token = response.get('access_token')
	token_type = response.get('token_type')
	expires_in = response.get('expires_in')

	updateOrCreateUserTokens(session_id, access_token, 
		token_type, expires_in, refresh_token)

def executeSpotifyApiRequest(session_id, endpoint, post_=False, put_=False):
	if isAuthenticated(session_id):
		token = getUserToken(session_id)
		headers = {'Content-Type': 'application/json', 
					'Authorization': "Bearer " + token.access_token}

		if post_:
			post(BASE_URL + endpoint, headers=headers)
		if put_:
			put(BASE_URL + endpoint, headers=headers)

		response = get(BASE_URL + endpoint, {}, headers=headers)

		try:
			return response.json()
		except:
			return{'Error: Issue with request'}
	else:
		return{'Error: Not Available'}
