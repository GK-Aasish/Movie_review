from django.urls import path
from core.views import home_view,register_view,login_view,movies_view,edit_movie_view,movie_detail_view

urlpatterns = [
    path("",home_view,name="home"),
    path("register",register_view,name="register"),
    path("login",login_view,name="login"),
    path("movies",movies_view,name="movies"),
    path("details/<int:id>",movie_detail_view,name="details"),
    path("edit/<int:id>",edit_movie_view,name="edit"),
]
