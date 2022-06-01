from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def homepage(request, tag_slug=None):
    posts = Post.published.all()

    paginator = Paginator(posts, 4)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if the page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    #search
    '''
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()
    '''
    return render(request, 'blog/post_list.html', {'posts': posts, 'page': page})
