User_input = input('Enter a message')
print(User_input)

'''Input: - Hello
World!
Output: - Hello
World!
'''

'''string = "Python Exceptions"
for s in string:
    if (s != o:
        print(s)
'''
string = "Python Exceptions"
'''for s in string:
    if (s != o):
        print(s)
'''

a = ["Python", "Exceptions", "try and except"]
try:
    for i in range(0, 4):
        print("The index and element from the array is", i, a[i])
except:
    print("Index out of range")


def reciprocal(num1):
    try:
        recipro = 1 / num1
    except ZeroDivisionError:
        print("We cannot divide by zero")
    else:
        print(recipro)


reciprocal(2)
reciprocal(0)
