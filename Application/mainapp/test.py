import os
os.environ['CLASSPATH'] = "./MusicScriptPrediction.jar"

import jnius

syso = jnius.autoclass('java.lang.System').out.println
arraylist = jnius.autoclass('java.util.ArrayList')

empathyscope = jnius.autoclass('synesketch.emotion.Empathyscope').getInstance()
emotionalstate = empathyscope.feel("I don't love you. You don't love me")
emotions = [ \
	emotionalstate.getAngerWeight(), \
	emotionalstate.getDisgustWeight(), \
	emotionalstate.getFearWeight(), \
	emotionalstate.getHappinessWeight(), \
	emotionalstate.getSadnessWeight(), \
	emotionalstate.getSurpriseWeight() \
]


for e in emotions :
	syso(e)
	

