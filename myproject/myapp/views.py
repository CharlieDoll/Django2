import requests
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def display_api_data(request):
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    response = requests.get(url)
    data = response.json()if response.status_code == 200 else {}
    print(data)
    return render(request, 'api_display/display.html', {'data': data})