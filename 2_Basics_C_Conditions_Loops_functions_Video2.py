i = 1
while i<5:
	print(i)
	i = i +1
'''Output:
1
2
3
4
'''


i = 1
while i<5:
	print(i)
	i = i +1
	if i==3:
		break
'''Output:
1
2
'''

List = [10,20,30,40,50]

for i in List:
	print(i)


'''Output :
10
20
30
40
50
'''
my_list = [3, 5, 6, 8, 4]
for iter_var in range( len( my_list ) ):
    print(my_list[iter_var])
'''Output:
3 5 6 8 4'''

for i in range(1,5):
	print(i)
'''Output:
1
2
3
4
'''

i = 1
for i in range(1,5):
	if i==3:
		continue
print(i)
'''Output:
1
2
4'''


