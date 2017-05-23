from django.shortcuts import render
from .models import Blogpost

def blog(request):
    blogpost = Blogpost.objects.order_by('-entry_date')
    return render(request, 'blog/blog.html', {'blogpost': blogpost})