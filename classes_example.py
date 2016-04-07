class Person():
    def __init__(self, name):
        # name is mangled/protected. Do not have direct access to the __name variable.
        self.__name = name

    # Getter for the name attribute.
    @property
    def name(self):
        print('Inside getter.')
        return self.__name

    # Setter for the name attribute.
    @name.setter
    def name(self, name):
        print('Inside setter.')
        self.__name = name

    # Method for the Person class that states the Person's name.
    def introduce(self):
        print('Hi, my name is ', self.name)

    # Method that does belongs to the class, but does not rely on any
    # of the class attributes, methods, or class objects themselves.
    @staticmethod
    def whatIam():
        print('I am a human being!')


class Student(Person):
    # initialize counter for class method used below
    count = 0

    def __init__(self, name, email, gpa):
        # Uses super to initialize the name through the root class.
        super().__init__(name)
        # Email is mangled/protected. Do not have direct access to the __email variable.
        self.__email = email
        self.gpa = gpa
        # Increment counter each time a new instance of the class is created.
        Student.count += 1

    # Since email only has a getter, the email cannot be changed after
    # the object is created.
    @property
    def email(self):
        return self.__email

    # Class method to print a Student's GPA
    def showGPA(self):
        print(self.name + '\'s GPA is', self.gpa)

    # Class method to print a Student's email address.
    def printEmail(self):
        print(self.name + '\'s email address is', self.__email)

    # Class method is a method that affects the class as a whole, not just
    # a single instance of the class
    @classmethod
    def kids(cls):
        # Returns how many instances of this class exist
        print('This class has', cls.count, 'students')


def main():
    # Create a Person object.
    peter = Person('Peter')
    print(peter.name, '\n')
    peter.name = 'Pete'

    # Call methods from Person class. Since introduce uses self.name, the
    # property method is called (getter).
    peter.introduce()
    # Call a static method. Method belongs to the class, but does not rely
    # on the class object, attributes, or methods of the class.
    peter.whatIam()
    print()

    steve = Student('Steve', 'steve@harvard.edu', 3.75)
    steve.showGPA()
    steve.printEmail()
    steve.name = 'Stephen'
    steve.gpa = 3.8
    steve.showGPA()

    jim = Student('Jim', 'Jim@unco.edu', 3.25)
    tom = Student('Tom', 'Tom@myspace.com', 2.5)

    # tom and jim (Students) inherit methods from their parent classes.
    tom.introduce()
    jim.whatIam()

    # Calls a class method to return a count of all of the student objects in Students
    Student.kids()

    # email attribute is protected, and cannot be change
    # steve.email = 'test'      this line won't work

if __name__ == '__main__':
    main()