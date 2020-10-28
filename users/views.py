""" Users views. """

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views
#Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

#Forms
from users.forms import SignupForm


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


class LoginView(auth_views.LoginView):
    """ Login view """
    template_name = 'users/login.html'


class SignupView(FormView):
    """ Users Sign up view """
    
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):
        """ Save form data """
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Update View """

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    
    def get_object(self):
        """ Return user's profile """
        return self.request.user.Profile
    
    def get_success_url(self):
        """ Return to user's profile """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username' : username})


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """ Logout view """

    template_name = 'users/logged_out.html'
