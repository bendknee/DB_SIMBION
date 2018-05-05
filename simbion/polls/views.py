from django.shortcuts import render

# Create your views here.
response = {}

def index(request):
	response["name"] = "Uvuvwevwe Ossas"
	html = "polls/polls.html"
	return render(request, html, response)