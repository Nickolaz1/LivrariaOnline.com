from django.shortcuts import render
from .models import Livro

def index(request):
    livros = Livro.objects.order_by('id')
    return render(request, 'livros/index.html', {'livros': livros})

def listar(request):
    livros = Livro.objects.order_by('id')
    return render(request, 'livros/lista.html', {'livros': livros})