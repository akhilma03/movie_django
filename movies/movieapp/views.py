from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie
from.forms import MovieForm
# Create your views here.

def index(request):
    
    movie = Movie.objects.all()
    context= {"movie":movie}
    
    return render(request,"movieapp/index.html",context)

def details(request,id):
     movies = Movie.objects.get(id=id)
     context= {"movies":movies}
     return render(request,"movieapp/detail.html",context)

def addmovie(request):
    if request.method =="POST":
        name = request.POST["name"]
        desc = request.POST["desc"]
        year = request.POST["year"]
        image = request.FILES["images"]
        movie = Movie(name=name, desc=desc, year=year,images=image)
        movie.save()
    return render(request,"movieapp/add.html")

def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('index') 
    context={
        
        'movie':movie,
        'form':form 
    }
    return render(request,"movieapp/edit.html",context)
    
def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        
        return redirect('index') 
    
    return render(request,"movieapp/delete.html")
    