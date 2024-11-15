from django.shortcuts import render

from .models import Post
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')
