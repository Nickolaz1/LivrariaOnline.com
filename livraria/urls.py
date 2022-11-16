from django.contrib import admin
from django.urls import path, include

from livros import views as livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', livros.index, name='index'),
    path('livros/', include('livros.urls'))
]
