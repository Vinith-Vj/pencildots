from django.shortcuts import render
from .models import Background, Team, Service, Gallery, About

# Create your views here.

def index(request):
    background = Background.objects.last() # Get the latest background image
    teams = Team.objects.all()
    services = Service.objects.all()
    galleries = Gallery.objects.all()
    about = About.objects.first()
    return render(request, 'index.html', {'background': background, 'teams': teams, 'services': services, 'galleries': galleries, 'about': about})