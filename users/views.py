""" Users views. """

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Forms
from users.forms import ProfileForm, SignupForm


def login_view(request):
    """ Login view """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
            
    return render(request, 'users/login.html')


def signup_view(request):
    """ Sign up view """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name = 'users/signup.html',
        context={'form' : form}
    )


@login_required
def update_profile(request):
    """ Update a user's profile view. """
    profile = request.user.profile

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form= ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    # Redirect to a success page.
    return redirect('login')