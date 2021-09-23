from django.db import models

class SpotifyToken(models.Model):
	user = models.CharField(max_length=50, unique=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	access_token = models.CharField(max_length=150, null=True)
	token_type = models.CharField(max_length=50, null=True)
	expires_in = models.DateTimeField(null=True)
	refresh_token = models.CharField(max_length=50, null=True)