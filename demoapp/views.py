from django.shortcuts import render_to_response
from demoapp.models import Post, Author, Category


def index(request):
    all_posts = Post.objects.all().order_by('-date')
    cat = Category.objects.all()
    template_data = {'posts' : all_posts, 'category': cat}
    return render_to_response('index.html', template_data)

def post_id(request,id):
    all_posts = Post.objects.filter(pk=id)
    posts = {'posts' : all_posts}
    return render_to_response('post.html', posts)

def show_more(request):
    all_posts = Post.objects.all().order_by('-date')
    cat = Category.objects.all()
    template_data = {'posts' : all_posts, 'category': cat}
    return render_to_response('show_more.html', template_data)
