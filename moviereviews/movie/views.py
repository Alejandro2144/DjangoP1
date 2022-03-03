from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1> Welcome to Home Page </h1>')
    #return render(request,'home.html', {'name': 'Alejandro Torres'})
    searchTerm = request.GET.get('searchMovie')
    return render(request,'home.html', {'searchTerm': searchTerm})
    

def about(request):
    return HttpResponse('<h1> Welcome to About Page </h1>')