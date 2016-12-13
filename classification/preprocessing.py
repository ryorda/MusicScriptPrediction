
emotions = [ 'disgust', 'fear', 'happy', 'sad', 'surprise', 'angry' ]

out	= open('emotions.arff' , 'w')
out.write("@RELATION\tsentence_emotions\n\n" )
out.write("@ATTRIBUTE\tsentence string\n")		
out.write("@ATTRIBUTE\temosi  {0}\n\n".format( "{ " + " , ".join(emotions) + " }" ) )		
out.write("@DATA\n")

for e in emotions :
	input 	= open('{0}.csv'.format(e) , 'r')
	for line in input :
		out.write( "' {0} ' , {1}\n".format(line.strip() , e) )
	input.close()
	
out.close()