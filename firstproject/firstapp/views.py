from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
	message = '<h1>Our first app</h1>'
	return HttpResponse (message)