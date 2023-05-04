from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Anime, Studio
from .forms import AnimeForm
from django.urls import reverse

# Create your views here.


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def animes_index(request):
    animes = Anime.objects.all()
    return render(request, 'animes/index.html', {
        'animes': animes
    })


def animes_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'animes/detail.html', {'anime': anime})

class Anime_Create(CreateView):
    model = Anime
    form_class = AnimeForm

class Anime_Update(UpdateView):
    model = Anime
    form_class = AnimeForm
    template_name = 'main_app/anime_form.html'

class Anime_Delete(DeleteView):
    model = Anime
    success_url = '/animes'

class Studio_Create(CreateView):
    model = Studio
    template_name = "main_app/studio_form.html"
    fields = '__all__'
    success_url = '/animes'