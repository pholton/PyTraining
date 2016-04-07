#!/usr/bin/python

from sys import argv

def main():
    script, from_file, to_file = argv

    indata = open(from_file).read()

    out_file = open(to_file, 'w')
    out_file.write(indata)

    out_file.close

if __name__ == '__main__':
    main()
