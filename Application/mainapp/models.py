from django.db import models

class Song(models.Model):
	writer = models.CharField(max_length=120)
	singer = models.CharField(max_length=120, primary_key = True)
	title = models.CharField(max_length=48, primary_key = True)
	year = models.PositiveSmallIntegerField()
	genre = models.CharField(max_length=32)
	lyric = models.TextField()
	
	def __unicode__(self):
		return '{0} , by : {1}'.format(self.title, self.singer)
	
	def __str__(self):
		return '{0} , by : {1}'.format(self.title, self.singer)
			
	
class EmotionSong(models.Model) :
	song = models.OneToOneField(Song, on_delete=models.CASCADE, related_name="related_song")
	anger = models.FloatField()
	disgust = models.FloatField()
	fear = models.FloatField()
	sadness = models.FloatField()
	happiness = models.FloatField()
	surprise = models.FloatField()
	
	def __unicode__(self):
		return 'emotion: {0} , by : {1}'.format(self.song.title, self.song.singer)
	
	def __str__(self):
		return 'emotion: {0} , by : {1}'.format(self.song.title, self.song.singer)