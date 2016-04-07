#!/usr/bin/python

from sys import argv

def main():
	filename = argv[1]
	
	print "We are going to erase %r." % filename
	print "If you don't want that, hit CTRL-C (^C)."
	print "If you do want that, hit ENTER."
	
	raw_input("?")
	
	print "Opening the file..."
	target = open(filename, 'w')
	
	print "Truncating the file. Goodbye!"
	target.truncate()
	
	print "Now I'm going to ask you for three lines."
	
	lines = []
	for i in range(3):
		lines.append(raw_input("line %d: " % (i + 1)))
	
	#lines.append(raw_input("line 1: "))
	#lines.append(raw_input("line 2: "))
	#lines.append(raw_input("line 3: "))
	
	print "I'm going to write these to the file."
	
	for line in lines:
		target.write(line + '\n')
	
	print "And finally, we close it."
	target.close()
	
if __name__ == '__main__':
	main()