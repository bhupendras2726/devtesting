from django.shortcuts import render

def blogHome(request):
    return render(request, 'blog/bloghome.html')
def blogPost(request, slug):
    return render(request, 'blog/blogpost.html', {'slug': slug})


# Create your views here.
