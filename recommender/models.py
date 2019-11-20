from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Searches'


    def __str__(self):
        return f'{self.created}: {self.search}'

class Song(models.Model):
    song_title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.artist} - {self.song_title}'
    
