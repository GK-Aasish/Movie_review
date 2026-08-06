from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from core.models import Movie,Genre,Reviews

# Create your views here.
def home_view(request):
    return render(request,"main/index.html")

def register_view(request):
    if request.method == "POST":
        errors = {}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username:
            errors['username']="Enter Username"
        if not email:
            errors['email']="Enter Email"
        if not password:
            errors['password']="Enter Password"
        if password != confirm_password:
            errors['confirm_password']="Passwords didn't match!"
        if errors:
            return render(request,"auth/register.html",{"errors":errors,"data":request.POST})

        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect("login")
    return render(request,"auth/register.html")

def login_view(request):
    if request.method == "POST":
        errors = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            errors['username'] = "Enter Your Username"
        if not password:
            errors['password'] = "Enter Your Password"

        if errors:
            return render(request,"auth/login.html",{"errors":errors,"data":request.POST})

        if not errors:
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    return render(request,"auth/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

def movies_view(request):
    query = request.GET.get('q')
    movies = Movie.objects.all()
    
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    p = Paginator(movies,1)
    p_number = request.GET.get('page')
    p_obj = p.get_page(p_number)
    
    return render(request,"main/movies.html",{"query":query,"p_obj":p_obj})

def movie_detail_view(request,id):
    movie = get_object_or_404(Movie, id=id)
    return render(request,"main/movie_details.html",{"movie":movie})

def edit_movie_view(request,id):
    get_genre = Genre.objects.all()
    movie = get_object_or_404(Movie,id=id)
    if request.method == "POST":
        errors = {}

        # get data from the frontend.
        title = request.POST.get('title')
        genre_id = request.POST.get('genre')
        description = request.POST.get('description')
        released_date = request.POST.get('released_date')

        if not title:
            errors['title'] = "Enter title"
        if not genre_id:
            errors['genre_id'] = "Enter genre"
        if not description:
            errors['description'] = "Enter description"
        if not released_date:
            errors['released_date'] = "Enter released_date"

        if errors:
            get_genre = Genre.objects.all()
            context = {
                "errors":errors,
                "get_genre":get_genre,
                "movie":movie
            }
            return render(request,"main/edit_movie.html",context)

        # Update Movie.
        movie.title = title
        movie.genre = get_object_or_404(Genre, id=genre_id)
        movie.description = description
        movie.released_date = released_date
        movie.save()
        return redirect("movies")
        
    return render(request,"main/edit_movie.html",{"get_genre":get_genre,"movie":movie})

def delete_movie_view(request,id):
    movie = get_object_or_404(Movie,id=id)
    movie.delete()
    return redirect("movies")

def add_movie_view(request):
    get_genre = Genre.objects.all()
    if request.method == "POST":
        errors = {}

        title = request.POST.get('title')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        released_date = request.POST.get('released_date')

        if not title:
            errors['title'] = "Enter title"
        if not genre:
            errors['genre'] = "Enter genre"
        if not description:
            errors['description'] = "Enter description"
        if not released_date:
            errors['released_date'] = "Enter released_date"

        if errors:
            return render(request,"main/add-movie.html",{"errors":errors,"data":request.POST,"get_genre":get_genre})

        # Save movie to the database
        movie = Movie.objects.create(
            title = title,
            genre = get_object_or_404(Genre, id=genre),
            description = description,
            released_date = released_date
        )
        return redirect("movies")
    return render(request,"main/add-movie.html",{"get_genre":get_genre})

def rating_view(request,id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        errors = {}
        rating_value = request.POST.get('rating')
        comment_value = request.POST.get('comment')

        if not comment_value:
            errors['comment'] = "Enter commetn"

        if not rating_value:
            errors['rating'] = " Enter Rating"

        if errors:
            return render(request,"main/movie_details.html",{"errors":errors,"data":request.POST,"movie":movie})

        if not errors:
            Reviews.objects.create(
                movie = movie,
                user = request.user,
                rating =int(rating_value),
                comment = comment_value
            )
            return redirect("details",id=movie.id)
        
    return redirect("details",id=movie.id)
        



