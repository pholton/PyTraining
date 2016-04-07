# Pros of named tuples
#   Looks and acts like an immutable object.
#   It is more space- and time-efficient than objects.
#   You can access attributes with dot notation instead of dictionary style
#       square brackets
#   You can use it as a dictionary key

from collections import namedtuple

# Creates a named tuple where Duck is the name, and bill and tail are
# the field names
Duck = namedtuple('Duck', 'bill tail')
# Creates a Duck named tuple called duck. Other method of creating a named
# tuple is shown below.
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

# Other method for creating a named tuple by using a dictionary
parts = {'bill': 'narrow yellow', 'tail': 'stubby'}
# **parts is a keyword argument. It extracts the keys and values from
# parts, and passes them to Duck(). It has the same affect as
# duck2 = Duck(bill = 'narrow yellow', tail = 'stubby')
duck2 = Duck(**parts)
print(duck2)

# Named tuples are immutable, however you can replace one or more fields
# and return another named tuple.
duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

all_ducks = [duck, duck2, duck3]
for fowl in all_ducks:
    print('This duck has a', fowl.bill, 'bill, and a', fowl.tail, 'tail.')
