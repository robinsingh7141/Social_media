from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from home.models import Contact, Signup, Post, Profile
from django.contrib import messages
from itertools import chain
import random


@login_required(login_url='signin')
def Home(request):
    # Fetch all posts of the currently logged-in user and pass them to the template
    user_feed = Post.objects.filter(user=request.user)
    context = {'posts': user_feed}  # Pass the posts with the key 'posts'
    return render(request, 'home.html', context)

@login_required(login_url='signin')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='signin')
def index(request):

    context = {
        'variable':'this is variable',
        'variable1':'robin is great'

    }
    return render(request, 'home.html', context)



# ... other view functions ...

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')

            # Hash the password before saving it
            hashed_password = make_password(password)

            # Create and save the new user
            new_user = User.objects.create(username=username, password=hashed_password, email=email)

            # Redirect to the '/signin' URL after successful signup
            return redirect('signin')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
                 
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("the username is {} and the password is {}".format(username,password))
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def Logout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def services(request):
    # return HttpResponse("this is services page")

    return render(request, 'service.html')

@login_required(login_url='signin')
def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact = Contact(name=name, phone = phone, email=email, comment=comment, date= datetime.today())
        contact.save()
        messages.success(request,"Thankyou for reaching out to us")
    return render(request, 'contact.html')

@login_required(login_url='signin')
def create_post(request):
    if  request.method == 'POST':
        content = request.POST.get('content')
        photo = request.FILES.get('photo')

        # Validate the form data, and save the post if valid
        if content and photo:
            new_post = Post(content=content, photo=photo, user=request.user)
            new_post.save()

        # Redirect back to the home page
        return redirect('home')

    # If the request is not POST, redirect to the home page
    return render(request, 'home.html')