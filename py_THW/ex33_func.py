#!/usr/bin/python

def for_loop(total, step):
    i = 0
    numbers = []
    while i < total:
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num

def main():
    for_loop(10, 2)


if __name__ == '__main__':
    main()
