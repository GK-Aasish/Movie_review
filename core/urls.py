from django.urls import path
from core.views import (
    home_view,
    register_view,
    login_view,
    movies_view,
    edit_movie_view,
    movie_detail_view,
    delete_movie_view,
    add_movie_view,
    logout_view,
    rating_view,
    )

urlpatterns = [
    path("",home_view,name="home"),
    path("register",register_view,name="register"),
    path("login",login_view,name="login"),
    path("logout",logout_view,name="logout"),
    path("movies",movies_view,name="movies"),
    path("movie/<int:id>",movie_detail_view,name="details"),
    path("edit/<int:id>",edit_movie_view,name="edit"),
    path("delete/<int:id>",delete_movie_view,name="delete"),
    path("add",add_movie_view,name="add_movie"),
    path("movie/<int:id>/review",rating_view,name="review")
]
