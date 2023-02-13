

def function(a):
	print(a)
function('Hello')
'''Output-
Hello'''

def my_function(*kids):
  print(kids[2])

my_function("Emil", "Tobias", "Linus")

'''Output -
Linus'''



def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
'''Output -
The youngest child is Linus'''


def my_function(country = "Norway"):
  print(country)

my_function()
my_function("Brazil")
'''Output-
Norway
Brazil
'''

def cal(a,b):
	return (a+b)
print(cal(5,5))
'''Output-
10
'''
def cal(a, b):
    a = 10
    b = 20
    return a+b

a = 5
b = 10
print(cal(a, b))
print(a)
print(b)
'''output:
30
5
10
'''

