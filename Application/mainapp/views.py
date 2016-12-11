from django.shortcuts import render, redirect
from django.http import HttpResponse

import os
os.environ['CLASSPATH'] = "predictlib.jar"
os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-8-oracle/"

import jnius


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
		emotion_names = [ "Anger", "Disgust", "Fear", "Happiness", "Sadness", "Surprise"]
		
		html = ''
		for i in range(6) :
			html = "{0}{1} : {2}\n".format(html, emotion_names[i], emotions[i])
		
		return HttpResponse(html)
	else :
		return redirect('/app/')

	