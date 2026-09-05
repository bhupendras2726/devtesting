from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from home.forms import ContactForm
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
     fname = request.session.get('fname')
     return render(request, 'home/index.html', {'fname': fname})

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

            return render(request, "home/contact.html",{"messages": "Your message has been sent successfully!"}
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
def handleSignup(request):
    if request.method =="POST":
        # Get the post parameters
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) < 10:
            return render(request, 'home/signup.html', {'error': 'Username must be at least 10 characters.'})
       
        if pass1 != pass2:
            return render(request, 'home/signup.html', {'error': 'Passwords do not match.'})

        #create user
        myuser = User.objects.create_user(username,email,pass1) 
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, f"Your {fname} account has been created successfully!")
        # Store fname in session
        request.session['fname'] = fname
        return redirect('home')
    else:
        return HttpResponse("404 - Not Found")



def handleLogout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('home')

def handleLogin(request):
  from django.shortcuts import redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta


def handleLogin(request):

    if request.method == "POST":

        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        # Get failed attempt information from session
        failed_attempts = request.session.get('login_attempts', 0)
        locked_until = request.session.get('locked_until')

        # Check whether account is temporarily locked
        if locked_until:
            locked_until = timezone.datetime.fromisoformat(locked_until)

            if timezone.now() < locked_until:
                messages.error(
                    request,
                    "Too many failed attempts. Please try again later."
                )
                return redirect('home')

            # Lock period has expired
            request.session['login_attempts'] = 0
            request.session.pop('locked_until', None)
            failed_attempts = 0

        user = authenticate(
            username=loginusername,
            password=loginpassword
        )

        if user is not None:

            # Successful login → reset attempts
            request.session['login_attempts'] = 0
            request.session.pop('locked_until', None)

            login(request, user)

            messages.success(
                request,
                f"Welcome {user.first_name}! You have been logged in successfully."
            )

            request.session['fname'] = user.first_name

            return redirect('home')

        else:

            # Wrong password
            failed_attempts += 1
            request.session['login_attempts'] = failed_attempts

            if failed_attempts >= 5:

                locked_until = timezone.now() + timedelta(minutes=10)

                request.session['locked_until'] = locked_until.isoformat()

                messages.error(
                    request,
                    "Too many failed login attempts. "
                    "You are blocked for 10 minutes."
                )

            else:

                remaining = 5 - failed_attempts

                messages.error(
                    request,
                    f"Invalid credentials. {remaining} attempts remaining."
                )

            return redirect('home')

    return HttpResponse("404 - Not Found")
