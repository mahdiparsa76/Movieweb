from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, context, loader
from .models import *


def index(request):
    movies=Movie.objects.all()
    generes=Genere.objects.all()
    context={'movies':movies,'generes':generes}
    return render(request,'movies/home.html',context)

def movie_details(request,slug):
    single_movie=Movie.objects.get(slug=slug)
    generes=single_movie.genere.all()
    actors=single_movie.actors.all()
    context={'single_movie':single_movie,'generes':generes,'actors':actors}

    return render(request,'movies/movie_details.html',context)

def actor_details(request,slug):
    actor=Actor.objects.get(slug=slug)

    context={'actor':actor}
    return render(request,'movies/actor.html',context)

def genre(request,genere):
    movie=Movie.objects.filter(genere__slug=genere)
    genres=Genere.objects.all()
    context={'movie':movie,'genres':genres}
    return render(request,'movies/genre.html',context)

def search(request):
    if request.method=="GET":
        q=request.GET.get("search")
    movies=Movie.objects.filter(title__icontains=q)
    context={'movies':movies}
    return render(request,'movies/home.html',context)

    