from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    posts_lists = list()
    for count, post in enumerate(posts):
        posts_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
        posts_lists.append(("<small>")+ str(post.body.encode('utf-8')) \
+"</small><br><br>" )

    return  HttpResponse(posts_lists)
