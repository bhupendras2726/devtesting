from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.forms import ContactForm
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

# def contact(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     desc = request.POST.get('desc')
    #     contact = Contact(name=name, email=email, phone=phone, description = desc)
    #     contact.save()
    #     return render(request, 'home/contact.html', {'message': 'Your message has been sent successfully!'})
    
    # return render(request, 'home/contact.html')
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            desc = form.cleaned_data["desc"]

            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                description=desc
            )
            contact.save()

            return render(request, "home/contact.html",{"message": "Your message has been sent successfully!"}
            )

    else:
        form = ContactForm()

    return render(request, "home/contact.html", {"form": form})

def about(request):
    return render(request, 'home/about.html')
def search(request):
    allPosts = Post.objects.filter(title__icontains=request.GET['query'])
    
    param ={"post": allPosts}
    return render(request, 'home/search.html',param)
       
  