'''This codes are dependent on the machine. so follow video thouroughly'''
file = open("demofile.txt", "r")
print(file.read())
print(file.read(5))
print(file.readline())
file.close()

file = open('demofile2.txt', 'a')
file.write('Now the file has been overwritten')
file.close()
File = open('demofile2.txt','r')
print(file.read())

import datetime
X = datetime.datetime.now()
print(x)

import math
x = math.sqrt(16)
print(x)
x = math.ceil(1.9)
y = math.floor(3.3)
print(x)
print(y)
print(math.pi)

import random
print(random.randint(1,1000))
import random as rnd
print(rnd.randint(1,1000))
from random import randint
print(randint(1,1000))
from random import *
print(randint(1,1000))

def greeting(name):
	print(name)

import again
again.greeting('Bishal')
