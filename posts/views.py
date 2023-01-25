from django.shortcuts import render
from noticias import noticia


def home(request):
    data = {}
    data['noticias_g1'] = noticia(0)
    data['noticias_olhar_digital'] = noticia(1)
    return render(request, 'posts/home.html', data)
