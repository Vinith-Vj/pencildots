from django.shortcuts import render
from .models import Header, Team, Service, Gallery, About, Logo

# Create your views here.

def index(request):
    header = Header.objects.last() # Get the latest background image
    logo = Logo.objects.last()
    teams = Team.objects.all()
    services = Service.objects.all()
    galleries = Gallery.objects.all()
    about = About.objects.first()
    return render(request, 'index.html', {'logo': logo, 'header': header, 'teams': teams, 'services': services, 'galleries': galleries, 'about': about})