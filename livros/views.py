from django.shortcuts import render

def index(request):
    return render(request, 'livros/index.html', {'nome': 'Nickolas'})