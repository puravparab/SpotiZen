from django.contrib import admin

# Register your models here.
from .models import SpotifyToken

@admin.register(SpotifyToken)
class SpotifyToken(admin.ModelAdmin):
	list_display = ('id', 'user', 'access_token', 'refresh_token', 'token_type', 'expires_in', 'created_at')
	fields = ['user', 'access_token', 'refresh_token', 'token_type', 'expires_in']