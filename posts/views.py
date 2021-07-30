from django.http import HttpResponse, request
from django.shortcuts import render
from .models import viewpost
# Create your views here.
def base(request):
	descs=viewpost.objects.all()
	return render(request,"index.html",{'vp':descs})

