from django.db import models

class Song(models.Model):
    author = models.CharField(max_length=30)
    singer = models.CharField(max_length=30)
    year = models.CharField(max_length=8)
    genre = models.CharField(max_length=30)
    lyric = models.TextField()
	
class EmotionSong(models.Model) :
	song = models.ForeignKey(Song, on_delete=models.CASCADE)
	anger = models.FloatField()
	disgust = models.FloatField()
	fear = models.FloatField()
	sadness = models.FloatField()
	happiness = models.FloatField()
	surprise = models.FloatField()