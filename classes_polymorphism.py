# Polymorphism allows different behavior for the same method depending on the class.
# In this case who and says are provided for each class, so depending on which class
# is calling the method, the results are different. This also works for classes that
# have no relation to one another. For example, who and says works on all of the Quote
# classes, but it also works on the BabblingBrook class.

class Quote():
    # Since the subclasses do not have __init__'s of their own, they
    # will default to the parent initialization method.
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


# This class is independent from the Quote classes, but polymorphism
# allows for who and says to still be called differently than the quote classes.
class BabblingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'babble'


# Helper function to return who says what. Takes the class object as an argument.
def who_says(obj):
    print(obj.who(), 'says', obj.says())


def main():
    hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
    who_says(hunter)

    hunted1 = QuestionQuote('Bugs Bunny', "What's up Doc")
    who_says(hunted1)

    hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
    who_says(hunted2)

    brook = BabblingBrook()
    who_says(brook)


if __name__ == '__main__':
    main()
