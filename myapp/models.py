from django.db import models

# Create your models here.

class Background(models.Model):
    image = models.ImageField(upload_to='backgrounds/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Team(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team/') 

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title
    

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')
    description = models.TextField()

    def __str__(self):
        return self.title
