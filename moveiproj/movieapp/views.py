from django.shortcuts import render
import requests
import json
# Create your views here.

my_id = '6b7cf43df64cb30d0a300b455b19a11b'

def home(request):
    url = 'https://api.themoviedb.org/3/trending/all/day?api_key='+my_id
    response = requests.get(url)
    resdata = response.text
    obj = json.loads(resdata)
    obj = obj['results']
    return render(request,'index.html',{'obj':obj})

def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=6b7cf43df64cb30d0a300b455b19a11b&language=en-US'
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {'resdata': resdata})