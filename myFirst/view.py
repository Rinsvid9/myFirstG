from django.http import HttpResponse
from django.shortcuts import render

def funk(request):
	return HttpResponse("Thus is about HttpResponse")

# def home(request):
# 	return HttpResponse("Thus is about home")

def dungen(request):
	return render(request, "home.html", {'greeting' : 'latherMan'}) 