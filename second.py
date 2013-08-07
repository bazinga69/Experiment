from sys import argv
script,filename = argv
print "We're goung to erase %r"%filename
print "opening file..."
target = open(filename,'rw+')
print "truncating the file. goodbye!"
#target.truncate()
print "now i am going to ask you three lines."
line = "%s\n%s\n"%(raw_input("line1?"),raw_input("line2? ")) 
target.write(line)
target.close()
target = open(filename)
print target.read()
target.close()
