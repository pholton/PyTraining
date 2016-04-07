#!/usr/bin/python

def main():
	my_name = "Peter Holton"
	my_age  = 31
	my_height = 70 # inches
	my_weight = 250 # lbs
	my_eyes = "Hazel"
	my_teeth = "White"
	my_hair = "Brown"
	
	print "Let's talk about %s." % my_name
	print "He's %d inches tall." % my_height
	print "He's %d pounds heavy." % my_weight
	print "Actually that is pretty heavy."
	print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
	print "His teeth are usually %s depending on the coffee." % my_teeth
	
	print "If I add %d, %d, and %d I get %d." % (
		my_age, my_height, my_weight, my_age + my_height + my_weight)

if __name__ == '__main__':
	main()