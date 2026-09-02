from django.shortcuts import render
from blog.models import Post

# def blogHome(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/bloghome.html', {'posts': posts})

# def blogPost(request, slug):
#     post = Post.objects.get(slug=slug)
#     return render(request, 'blog/blogpost.html', {'post': post})


# Create your views here.
def blogHome(request):
    posts = Post.objects.all()
    print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'blog/bloghome.html', {'posts': posts})


def blogPost(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/blogpost.html', {'post': post})
