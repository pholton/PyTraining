#!/usr/bin/python

from sys import argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),

def main():
    input_file = argv[1]

    current_file = open(input_file)

    print "First let's print the whole file:\n"
    print_all(current_file)

    print "Now let's rewind, kind of like a tape."
    rewind(current_file)

    print "Let's print three lines:"

    for i in range(3):
        print_a_line(i + 1, current_file)

if __name__ == '__main__':
    main()