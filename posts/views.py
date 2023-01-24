from django.shortcuts import render
from noticias import noticia


def home(request):
    data = {}
    data['noticias'] = noticia(0)
    data['noticias'] += noticia(1)
    return render(request, 'posts/home.html', data)
