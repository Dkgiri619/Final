from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    porto = Portfolio.objects
    return render(request, 'portfolio.html', { 'portfolio': porto })
