from django.shortcuts import redirect, render
from blog.models import Post
from django.utils.text import slugify
from blog.models import Blogcomment
from django.contrib import messages
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
    comments =Blogcomment.objects.filter(post=post, parent=None)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/blogpost.html', context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("post_id")
        post = Post.objects.get(sno=postsno)
        print(comment, user,postsno, post)
        
        comment = Blogcomment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")
        return redirect(f"/bloghome/{post.slug}")
    else:
        return redirect("/bloghome/")

        
