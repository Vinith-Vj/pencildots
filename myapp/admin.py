from django.contrib import admin
from .models import Header, Team, Service, Gallery, About, Logo

# Register your models here.

admin.site.register(Header)

admin.site.register(Logo)

admin.site.register(Team)

admin.site.register(Service)

admin.site.register(Gallery)

admin.site.register(About)