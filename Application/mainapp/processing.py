from . import configs
from . import models

import os
os.environ['CLASSPATH'] = "predictlib.jar"
os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-8-oracle/"

import jnius
import json
import statistics

def findmatchsong(scripttext) :
	empathyscope = jnius.autoclass('synesketch.emotion.Empathyscope').getInstance()
	emotionalstate = empathyscope.feel(scripttext)
	emotions = [ \
		emotionalstate.getAngerWeight(), \
		emotionalstate.getDisgustWeight(), \
		emotionalstate.getFearWeight(), \
		emotionalstate.getHappinessWeight(), \
		emotionalstate.getSadnessWeight(), \
		emotionalstate.getSurpriseWeight() \
	]

	emotion_names = [ "anger", "disgust", "fear", "happiness", "sadness", "surprise"]
	normalized_emotion_names = [ "normalizedAnger", "normalizedDisgust", "normalizedFear", "normalizedHappiness", "normalizedSadness", "normalizedSurprise"]

	vars = { 'text' : scripttext}
	mean_data = statistics.mean(emotions)
	std_data = statistics.pstdev(emotions)

	normalized_emotions = []
	for i in range(6) :
		vars[emotion_names[i]] =  "{0:.1f}".format(emotions[i] * 100)
		if (std_data > 0) :
			z = (emotions[i] - mean_data)*1.0/std_data
		else :
			z = 0
		vars[normalized_emotion_names[i]] = z
		normalized_emotions.append(z)
	
	emotionsongs = models.EmotionSong.objects.all()
	result = None
	for es in emotionsongs :
		euc_dist = get_euclidian_dist(es, normalized_emotions)
		if (result is None) :
			result = [ ( euc_dist , es.song ) ]
		else :
			length = min(len(result) , 10)
			for i in range(length) :
				if (result[i][0] > euc_dist ) :
					result.insert(i, (euc_dist, es.song) )
					break
	
	vars['result'] = []
	
	for i in range(min(len(result) , 10)) :
		song = result[i][1]
		vars['result'].append({\
			'rank' : ( i + 1 ), \
			'title' : song.title, \
			'writer' : song.writer, \
			'singer' : song.singer, \
			'year' : song.year, \
			'genre' : song.genre, \
		})
		
	return vars
	
def get_euclidian_dist(emotionalstate, normalized_emotions) :

	emotions = [ \
		emotionalstate.anger, \
		emotionalstate.disgust, \
		emotionalstate.fear, \
		emotionalstate.happiness, \
		emotionalstate.sadness, \
		emotionalstate.surprise \
	]
	
	mean_data = statistics.mean(emotions)
	std_data = statistics.pstdev(emotions)
	
	total = 0
	for  i in range(len(emotions)) : 
		if (std_data > 0) :
			z = ( emotions[i] - mean_data ) * 1.0 / std_data
		else :
			z = 0
		total = total + z - normalized_emotions[i]

	return total
		
def recomputeall() :
	configs.isRecomputingAll = True
	
	print('recomputingAll : ' + str(configs.isRecomputingAll) )
	
	models.EmotionSong.objects.all().delete()
	songs = models.Song.objects.all()
	empathyscope = jnius.autoclass('synesketch.emotion.Empathyscope').getInstance()
	
	for song in songs :
		emotionalstate = empathyscope.feel(song.lyric)
		
		models.EmotionSong.objects.create( \
			song = song, \
			anger = emotionalstate.getAngerWeight(), \
			disgust = emotionalstate.getDisgustWeight(), \
			fear = emotionalstate.getFearWeight(), \
			happiness = emotionalstate.getHappinessWeight(), \
			sadness = emotionalstate.getSadnessWeight(), \
			surprise = emotionalstate.getSurpriseWeight() \
		)
		
	configs.isRecomputingAll = False
	
	print('recomputingAll : ' + str(configs.isRecomputingAll) )
	
def addnewsong(writer, singer, title,  year, genre, lyric) :
	(song, iscreated) = models.Song.objects.update_or_create( writer=writer, singer=singer, title=title, year=year, genre=genre, lyric=lyric)
		
	empathyscope = jnius.autoclass('synesketch.emotion.Empathyscope').getInstance()
	emotionalstate = empathyscope.feel(lyric)
	
	models.EmotionSong.objects.update_or_create ( \
		song = song, \
		anger = emotionalstate.getAngerWeight(), \
		disgust = emotionalstate.getDisgustWeight(), \
		fear = emotionalstate.getFearWeight(), \
		happiness = emotionalstate.getHappinessWeight(), \
		sadness = emotionalstate.getSadnessWeight(), \
		surprise = emotionalstate.getSurpriseWeight() \
	)
	