from django.shortcuts import redirect, render
from blog.models import Post
from django.utils.text import slugify

# Create your views here.

def blogHome(request):
    posts = Post.objects.all()
    print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'blog/bloghome.html', {'posts': posts})
def newPost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        keywords = request.POST.get('keywords')
        slug = slugify(title)

        post = Post(title=title, content=content, author=author, slug=slug)
        post.save()
        # return render(request, 'blog/newpost.html')
        return redirect('/bloghome/' + slug)

    return render(request, 'blog/newpost.html')


def blogPost(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'blog/blogpost.html', {'post': post})
