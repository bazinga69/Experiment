from sys import argv

script,from_,to_ = argv

text = open(from_).read()
open(to_,'w').write(text+"hella bithces")
txt = open(from_,'a+')
txt.readline()
txt.write("I am her")
hella bithcesI am her