from django.shortcuts import render, redirect
from requests import get

from spotify.utils import isAuthenticated

def welcome(request):
	session_id = request.session.session_key
	if isAuthenticated(session_id):
		return redirect('frontend-main')
	return render(request, 'frontend/home.html')

def main(request):
	session_id = request.session.session_key

	if not isAuthenticated(session_id):
		return redirect('frontend-welcome')
	return render(request, 'frontend/main.html')