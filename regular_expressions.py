import re
import string

result = re.match('You', 'Young Frankenstein')
print(result.group())

# Store expression as a variable
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')

# The '^' is somewhat redundant because match only matches from the
# beginning of the line.
m = re.match('^You', 'Young Frankenstein')
if m:  # Check if match returned an object
    print(m.group(), '\n')

printable = string.printable

print('All digits in string.printable (\d):')
print(re.findall(r'\d', printable))

print('All digits, letters, and underscore in printable (\w):')
print(re.findall(r'\w', printable))

print('All whitespaces in printable')
print(re.findall(r'\s', printable), '\n')

print('Regex also works with other unicode characters')
x = 'abc' + '-/+' + '\u00ea' + '\u0115'
print('x =', x)

print('All digits, letters, and underscores in x:')
print(re.findall(r'\w', x), '\n')

source = 'I wish I may, I wish I might Have a dish of fish tonight'
print(source)

print('Find "wish"')
print(re.findall(r'wish', source))

print('Find "wish" or "fish"')
print(re.findall(r'[wf]ish', source))

print('Find "I" followed by "wish"')
print(re.findall(r'I (?=wish)', source))

print('Find "wish" preceded by "I"')
print(re.findall(r'(?<=I) wish', source), '\n')

m = re.search(r'(. dish\b).*(\bfish)', source)
print('m.group:', m.group())
print('m.groups:', m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print('m.group:', m.group())
print('m.groups:', m.groups())
print('m.group(\'DISH\'):', m.group('DISH'))
print('m.group(\'FISH\'):', m.group('FISH'))