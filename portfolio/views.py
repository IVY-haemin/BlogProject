from django.shortcuts import render,get_object_or_404 ,redirect
# Create your views here.
from django.utils import timezone

from .models import Portfolio

# Create your views here.

def portfolio(request):
    portfolios=Portfolio.objects
    return render(request,'portfolio.html',{'portfolios': portfolios})

def upload(request):
    return render(request, 'upload.html')

def createport(request):
    portfolio = Portfolio()
    portfolio.title = request.GET['title']
    portfolio.description = request.GET['description']
    portfolio.image=request.GET['image']

    portfolio.save()
    return redirect('/portfolio' )