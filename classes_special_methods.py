class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("', self.text, '")'


first = Word('ha')
second = Word('HA')
print('%s' % (first == second))
third = Word('eh')
print('%s\n' % (first == third))

print(first)