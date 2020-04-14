from django.shortcuts import render


#create your views here.
from django.http import HttpResponse
from.models import Movie





#def index(request):
# movies = Movie.objects.all()
# return render(request)

#def index(request):
#    my_dict = {"insert_me": "I am from views.py"}
#    return render(request, 'views/index.html',context=my_dict)




def index(request):
    movies = Movie.objects.all()
    return render(request,'views/index.html', {'movies': movies})


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'views/details.html', {'movie': movie})






