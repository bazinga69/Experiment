from sys import argv
from os.path import exists

script,from_file,to_file = argv ; open(to_file,'w').write(open(from_file).read())

#print "copying from %s to %s" %(from_file,to_file)

#in_file = open(from_file)
#indata = in_file.read()

#print "The input file is %d byted long" % len(indata)
#print "the output file exists? %r"%exists(to_file)

#out_file = open(to_file,'w')
#out_file.write(indata)
#out_file.truncate()
#print "Allright, all done"
