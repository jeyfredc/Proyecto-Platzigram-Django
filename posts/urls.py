""" Posts urls """

#Django
from django.urls import path

#Views
from posts import views

urlpatterns = [

    path(
        route='posts/feed/',
        view= views.PostFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/new/',
        view= views.PostCreateView.as_view(),
        name='create_post'
    ),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )

]