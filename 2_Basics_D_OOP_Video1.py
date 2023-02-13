

class Person:
	x = 5
p1 = Person()
'''print(p1.x)
Output- 5'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

'''Output-
John
36
'''


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
'''Output:-
Hello my name is John
'''
p1.age = 40
print(p1.age)
'''Output:-
40'''


class Person:
    firstname = "john"
    lastname = "doe"
    def printname(self):
        print(self.firstname, self.lastname)
class Child(Person):
    pass
x = Child()
x.printname()


class Person:
    def __init__(self):
        self.firsname = "John"
        print(self.firstname)
class Child(Person):
    def __init__(self):
        self.firstname = "Albert"
        print(self.firstname)
x = Child()
'''Output : -
Albert'''


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
'''Output:-
Welcome Mike Olsen to the class of 2019'''


