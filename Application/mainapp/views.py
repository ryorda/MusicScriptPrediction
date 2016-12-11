from django.shortcuts import render, redirect
from django.http import HttpResponse

import os
os.environ['CLASSPATH'] = "predictlib.jar"
os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-8-oracle/"

import jnius
import json
import statistics

def index(req) :
	return render(req, 'mainapp/index.html', None)
	
def result(req) :
		
	if (req.method == 'POST' ) :
		
		scripttext 	= req.POST['scripttext']
		
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
		
		for i in range(6) :
			vars[emotion_names[i]] =  "{0:.1f}".format(emotions[i] * 100)
			if (std_data > 0) :
				vars[normalized_emotion_names[i]] = (emotions[i] - mean_data)*1.0/std_data
			else :
				vars[normalized_emotion_names[i]] = 0
			
		# return HttpResponse(json.dumps(vars))
		print(vars)
		return render(req, 'mainapp/result.html', vars)
	else :
		return redirect('/app/')

	