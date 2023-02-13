Mylists = [10,5,20]
Mylists = [True,False,True]
Mylists = ['john','roy','pritom']
print(Mylists)

Mylist = ['abc',10,'roy',True]

Mylist[0] = "abc"
Mylist[1] = 10
Mylist[2] = "roy"
Mylist[3] = True

print(Mylist[0])
print(Mylist[1])
print(Mylist[2])
print(Mylist[3])

List = [0,1,2,3,4,5]
print(List[0:])
    #1,2,3,4,5
print(List[:])
    #0,1,2,3,4,5
print(List[1:4])
    #1,2,3
print(List[:4])
    #0,1,2,3

List = [0,1,2,3,4,5]
#Index  -6,-5,-3,-2,-1


List = [1,2,3,4,5]
print(len(List))
List.append(40)
List.remove(2)
List.sort()
'''Output -
5
List = [1,2,10,4,5,40]
List = [1,10,4,5,40]
List = [1,4,5,10,40]'''


tuple_1 = ("Python", "tuples", "immutable", "object")
tuple_2 = (23, 42, 12, 53, 64)
tuple_3 = "Python", "Tuples", "Ordered", "Collection"
Empty_tuple = ()
My_tuple = (50,)

Set = {10,50,30}
print(Set)
'''Output : -
{10,50,30}'''

Set1 = {10,20}
Set2 = {20,30}
print(Set1|Set2)
'''Output:-
{10,20,30}'''

Set1 = {10,20}
Set2 = {20,30}
print(Set1&Set2)
'''output:-
{20}'''

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
'''Output
<class 'dict'>
Printing Employee data ....
{'Name': 'John', 'Age': 29, 'salary': 25000, 'Company': 'GOOGLE'}'''


Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(Employee["Name"])
print(Employee["Age"])
print(Employee["salary"])
print(Employee["Company"])
'''Output:
John
29
25000
GOOGLE'''


Dict = {
	'Name' : 'john'
}
Dict['Name'] = 'Alvarez'
print(Dict)
'''Output:
Dict = {“Name” : “Alvarez”}'''


Dict = {1: 'JavaTpoint', 2: 'Peter', 3: 'Thomas'}
pop_ele = Dict.pop(3)
print(Dict)
'''Output:
{1: 'JavaTpoint', 2: 'Peter'}'''




print("Hello")


a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)




a = "Hello, World!"
print(a[1])


a = "Hello, World!"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)




