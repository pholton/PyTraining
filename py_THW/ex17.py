#!/usr/bin/python

from sys import argv
from os.path import exists

def main():
    from_file = argv[1]
    to_file = argv[2]

    print "Copying from %s to %s" % (from_file, to_file)
    
    # Do this in one line
    #in_file = open(from_file)
    #indata = in_file.read()
    indata =open(from_file).read()
    
    print "The input file is %d bytes long" % len(indata)
    
    print "Does the output file exist? %r" % exists(to_file)
    print "Ready, hit ENTER to continue, CTRL-C to abort."
    raw_input()

    out_file = open(to_file, 'w')
    out_file.write(indata)

    print "Alright, all done."

    out_file.close()

if __name__ == '__main__':
    main()
