from importlib.resources import path
from django.shortcuts import render
from .models import Profile
# We can get rid of the below UserCreationForm in the registerUser method
# and use this. (Why?) same functionality with modified fields
from .forms import CustomUserCreationForm 

# Create your views here.

# These are for authentications
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.models import User

# This is for flash messages
from django.contrib import messages

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context=context)


def logoutUser(request):
    # this one is going to delete the session
    logout(request)
    messages.error(request, 'User was logged out.')
    return redirect('login')


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description__exact="")

    context = {'profile': profile, "topSkills": topSkills, "otherSkills": otherSkills}
    return render(request, 'users/user-profile.html', context=context)


# Don't name it login because it's defined in django's scope
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')


    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            # print('Username does not exist')
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        # This will take in the user and pass and it will make sure the
        # pass matches the username and it will return back either the user
        # instance or None

        if user:
            # login function is going to create a session for this user
            # in the database. Then it's also going to get that session
            # and it's going to add that into our browser's cookies
            login(request, user)
            # So if a user successfully logs in, let's go ahead and redirect
            # the user
            return redirect('profiles')
            # this is not very friendly, since it just redirects users back
            # to the home page! But what if a user was checking some page
            # and that page needs an authentication, so the user don't get
            # lost
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, 'users/login_register.html')
    # next we need to manage its routing

def registerUser(request):
    page = 'register'
    
    # It's not clean code putting imports here, but it's for 
    # educational purposes
    # from django.contrib.auth.forms import UserCreationForm
    # form = UserCreationForm()
    form = CustomUserCreationForm()


    # Basically a model form based around user and it's designed to
    # actually add a user to the database
    
    # Whenever a post method is sent, we can check 
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # this is just going to check that everything is correct
            # all the fields match up and no data has been manipulated
            # or anything like that -_-
            user = form.save(commit=False)
            # making all usernames lowercase
            user.username = user.username.lower()
            user.save()
            # Now that the user has officially been added to the database and
            # saved, let's go ahead and put a flash message here and let the
            # user now that the account was actually created

            messages.success(request, 'User account was created!')

            login(request, user)
            # this is gonna create a session-based token in the database
            # and it's gonna added to the cookies
            return redirect('profiles')
        else:
            messages.error(request, "An error has occurred during registration")

    context = {"page":page, "form": form}
    return render(request, 'users/login_register.html', context)