from django.db import models
from django.contrib import admin

'''
field:
    Char
    Int
    Float
    Boolean

'''
#  Migration steps
# 1- Make migrations
# 2 - (migrate) apply migrations

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length = 225)
    star =models.CharField(max_length = 255)
    release_year = models.IntegerField()
    price = models.FloatField()
    in_stock = models.IntegerField()
    # have 1 to many relations with genre
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    in_4k = models.BooleanField()
    director = models.CharField(max_length = 255)
    image_url = models.TextField()

    #def_str_(self):
    # return str(self.release_year) + self.title

    # lets say you wanst add a new colomn for the genre list , to display the ID  
    # customize the string representation of the genre objects
    # on models

    ##Customize genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    #create classes to customise how admi n models

class MovieAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id', 'release_year', 'title', 'genre')
    #exclude = ('in_stock', 'price')
        #fields = ('genre', 'title', 'directo)




