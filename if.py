print "you enter a dark room with two doors"

door = raw_input("> ")

if door == "1":
	print "there;s a giant bear here eating cheese cake"
	print "1.Take the cake"
	print "2.Screame at the bear"

	bear = raw_input('> ')
	
	if bear == "1":
		print "The bear eats off your space"
	elif bear == "2":
		print "the bear eats your legs"
	else :
		print "Well, doing %s the bear runs away"% bear

elif door == "2":
	print "You stae"
	print "bluberr"
	print "yello jacket"

	insanity = raw_input("> ")
	
	if (insanity == "1" or insanity == "2") and 1 == 1 :
		print "tested you bastard"
	else :
		print "this is what i got"

elif 2<int(door)<10 :
	print "nothing happens"
elif int (door) in range(10,20):
	print "the end"

