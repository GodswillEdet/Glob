from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def homepage(request):
    return render(request, 'blog/post_list.html', {'Post': Post.objects.all, 'Pot': Post.objects.dates('publish', 'day', order='DESC')})