from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import configs
from . import processing

import json
import _thread

def index(req) :
	return render(req, 'mainapp/index.html', None)
	
def result(req) :
		
	if (req.method == 'POST' ) :
		
		scripttext 	= req.POST['scripttext']
		
		vars = processing.findmatchsong(scripttext)
		print(vars)
		
		return render(req, 'mainapp/result.html', vars)
	else :
		return redirect('/app/')


def entrysong(req) :
	if (req.method == 'GET' ) :
		
		username = req.GET['username']
		password = req.GET['password']
		writer = req.GET['writer']
		singer = req.GET['singer']
		title = req.GET['title']
		year = req.GET['year']
		genre = req.GET['genre']
		lyric = req.GET['lyric']
		
		user = authenticate(username=username, password=password)
		
		if (user is None) :
			return HttpResponse(status = 401, content=json.dumps({'status' : 401, 'message' : 'Unauthorized user'}))
		
		if ( (writer is None) or (singer is None) or (title is None) or (year is None) or (genre is None) or (lyric is None) ) :
			return HttpResponse(status = 400, content=json.dumps({'status' : 400, 'message' : 'Bad request'}))
		
		_thread.start_new_thread( processing.addnewsong, (writer, singer, title, year, genre, lyric) )
		
		return HttpResponse(status = 200, content=json.dumps({'status' : 200, 'message' : 'OK', 'info' : 'we can\'t make sure the success of database entry'}))
		
	else :
		return HttpResponse(status = 400, content=json.dumps({'status' : 400, 'message' : 'Bad request'}))
		
def recomputeall(req) :
	username = req.GET['username']
	password = req.GET['password']
	
	user = authenticate(username=username, password=password)
	
	if (user is None) :
		return HttpResponse(status = 401, content=json.dumps({'status' : 401, 'message' : 'Unwriterized user'}))
	
	if (not configs.isRecomputingAll) :
		configs.isRecomputingAll = True
		_thread.start_new_thread( processing.recomputeall , ())
		return HttpResponse(status = 200, content=json.dumps({'status' : 200, 'message' : 'OK'}))	
	else :
		return HttpResponse(status = 102, content=json.dumps({'status' : 102, 'message' : 'Process is running on background'}))
		
		
def debug(req) :
	user = authenticate(username='-', password='-')
	configs.recomputeall = False
	return HttpResponse(status=200, content=json.dumps({'status' : 200, 'message' : 'OK'}))