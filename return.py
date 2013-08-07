from __future__ import division
def add(on,tw):
	print "Adding %d and %d"%(on,tw)
	return on+tw
def sub(on,tw):
	print "substracing %d and %d"%(on,tw)
	return on-tw
def mul(a,b):
	print "muling %d and %d"%(a,b)
	return a*b

def div(a,b):
	print "dividing %d and %d"%(a,b)
	#print "Aritmentic","bitches",3
	print "division is %f"%(a/b)
	return a/b
age = add(20,2.3)
weight = sub(80,4)
height = mul(1,6)
iq = div(200,1.5)
print "age:%d weight:%d height:%d iq:%d"%(age,weight,height,iq)

what = add(age,sub(height,mul(weight,div(iq,2))))
print "That becomes",what,"can you do it bu hand",
print "thats how [you do it"

