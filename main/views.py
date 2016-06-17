from django.shortcuts import render
from django.http import HttpResponse
from main.models import Test

# Create your views here.

def test(request):
	objects = Test.objects.all()
	value = objects[0]
	return HttpResponse("<h1>" + value + "</h1>")
