from django.shortcuts import render
from requests import get

def welcome(request):
	return render(request, 'frontend/home.html')

def main(request):
	return render(request, 'frontend/main.html')

	