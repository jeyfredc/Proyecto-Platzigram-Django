""" Users urls """

#Django
from django.urls import path
#Views
from users import views

urlpatterns = [

    #Mangement
    path(
        route = 'login/', 
        view = views.LoginView.as_view(),
        name = 'login'
    ),

    path(
        route = 'logout/',
        view = views.LogoutView.as_view(), 
        name = 'logout'
    ),

    path(
        route = 'signup/', 
        view= views.SignupView.as_view(), 
        name = 'signup'
    ),

    path(
        route = 'me/profile/', 
        view = views.UpdateProfileView.as_view(), 
        name = 'update_profile'
    ),

    #posts
    path(
        route = '<str:username>/',
        view = views.UserDetailView.as_view(),
        name = 'detail'
    ),
]