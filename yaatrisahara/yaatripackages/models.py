from django.db import models
class Package(models.Model):

    title = models.CharField(max_length=200)
    content = models.CharField(max_length=600)
    pricing = models.IntegerField(null=True)
    image = models.ImageField(default='default.jpg',upload_to='package_images')

    def __str__(self):
        return self.title

class Location(models.Model):
    place_name = models.CharField(max_length=100)
    package = models.ManyToManyField(Package)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.place_name
# Create your models here.
