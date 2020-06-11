from django.shortcuts import render
from .models import Blog

def blogs(request):
    allblogs = Blog.objects
    return render(request, 'blogs.html', {'allblogs': allblogs})