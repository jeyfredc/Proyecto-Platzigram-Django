""" Users urls """

#Django
from django.urls import path
from django.views.generic import TemplateView

#Views
from users import views

urlpatterns = [

    #posts
    path(
        route = '<str:username>/',
        view = TemplateView.as_view(template_name='users/detail.html'),
        name = 'detail'
    ),

    #Mangement
    path(
        route = 'users/login/', 
        view = views.login_view,
        name = 'login'
    ),

    path(
        route = 'users/logout/',
        view = views.logout_view, 
        name='logout'
    ),

    path(
        route = 'users/signup/', 
        view= views.signup_view, 
        name='signup'
    ),

    path(
        route = 'users/me/profile/', 
        view = views.update_profile, 
        name='update_profile'
    ),

]