from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):
	return render_to_response('login.html')