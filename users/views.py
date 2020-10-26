""" Users views. """

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

#Models
from django.contrib.auth.models import User
from posts.models import Post

#Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view """

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ User detail view. """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        # Add in a QuerySet of all the books
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


def login_view(request):
    """ Login view """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
            
    return render(request, 'users/login.html')


def signup_view(request):
    """ Sign up view """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
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

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)

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
    return redirect('users:login')