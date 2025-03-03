from django.db import models
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

# Create your models here.

class Header(models.Model):
    image = models.ImageField(upload_to='header/')
    catchphrase = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.image = self.compress_image(self.image)
        super(Header, self).save(*args, **kwargs)

    def compress_image(self, image):
        return compress_image_helper(image)

    def __str__(self):
        return self.catchphrase
    
class Logo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='logo/')

    def save(self, *args, **kwargs):
        self.image = self.compress_image(self.image)
        super(Logo, self).save(*args, **kwargs)

    def compress_image(self, image):
        return compress_image_helper(image)

    def __str__(self):
        return self.title
    
    
class Team(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team/') 

    def save(self, *args, **kwargs):
        self.image = self.compress_image(self.image)
        super(Team, self).save(*args, **kwargs)

    def compress_image(self, image):
        return compress_image_helper_team(image)

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def save(self, *args, **kwargs):
        self.image = self.compress_image(self.image)
        super(Service, self).save(*args, **kwargs)

    def compress_image(self, image):
        return compress_image_helper(image)

    def __str__(self):
        return self.title
    

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def save(self, *args, **kwargs):
        self.image = self.compress_image(self.image)
        super(Gallery, self).save(*args, **kwargs)

    def compress_image(self, image):
        return compress_image_helper_team(image)

    def __str__(self):
        return self.title
    

class About(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.image = self.compress_image(self.image)
        super(About, self).save(*args, **kwargs)

    def compress_image(self, image):
        return compress_image_helper(image)

    def __str__(self):
        return self.title



def compress_image_helper(image):
    img = Image.open(image)

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    output_io_stream = BytesIO()
    img.save(output_io_stream, format='WEBP', quality=50)
    output_io_stream.seek(0)

    return ContentFile(output_io_stream.read(), name=image.name)


def compress_image_helper_team(image):
    img = Image.open(image)

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    output_io_stream = BytesIO()
    img.save(output_io_stream, format='WEBP', quality=20)
    output_io_stream.seek(0)

    return ContentFile(output_io_stream.read(), name=image.name)

