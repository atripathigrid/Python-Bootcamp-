#Python Practice 
#DATA TYPES 
#int - Integer (whole numbers like 3,400,5000)
#float - Floating Point (Numbers with decimal point)
#str - Strings (Ordered Sequence of a character ("Hello", "Achintya"))
#list - Lists (Ordered sequence of objects [10, "Hi", 200.4]) 
#dict - Dictionaries (Unordered key:value pairs {"myname":"value", "name":"Achintya" })
#tup - Tuples (Ordered IMmmutable sequence of objects (10,"Achintya",100.5))
#set - Sets (Unordered collection of unique objects {"E", "F"})
#bool - Booleans (Logical value indicates True or False)

#Difference between floating point and integers
#Integers has no decimal points in it but floating points are the numbers which has decomal points in it.

# String Properties and Methods 
#Immutability of Strings - You cannot mutate or you cannot change.
#Concatinatng two strings
name = 'Tim'
last_letters = name[1:]
last_letters
's' + last_letters

x = 'Good Morning'
x = x + " I am Achintya Tripathi."
x

#String Formatting for printing
#There are 2 methods of string formatting 
# .format() method
# f-strings (formatted string literals)

# Formatting with .format() method
#A good way to format objects into your strings for print statements is with the strings .format method
# The syntax is:
print('Hi Achintya Tripathi this {}' .format('side'))
print('Hi Achintya {} {} {}' . format ('Tripathi','this' ,'side'))
print('The {} {} {}' .format ('fox', 'brown', 'quick'))
print('The {2} {1} {0}' .format ('fox', 'brown', 'quick'))

# Float formatting with .format() method
# The syntax is: "value:width.precision f"
result = 100/333
result
print('The result is {}' .format(result))
print('The result is {r}' .format(r = result))
print('The result is {r:1.3f}' .format(r = result))
print('The result is {r:1.6f}' .format(r = result))

# F-strings (Formatted Strings Literals)
name = "Achintya Tripathi"
name 
print ('Hi, my name is {}' .format(name)) #This was .format formatting
print(f'Hi, my name is {name}') #f-strings formatting
name = "Achintya Tripathi"
age = 23
print(f'Hi, my name is {name} and I am {age} years old') #f-strings formatting with multiple strings

#Lists 
#List are ordered sequences ta can hold a variety of object types. They use [] and commmas to separate objects in the lists. List also supports slicing and indexing.
my_list = [1,2,3]
my_list = ['string', 100, 200.5]
len(my_list)
my_list[2]
my_list[1:]
my_list

#We can also concantenate in lists 
mylist = ['one', 'two', 'three']
anotherlist = ['four', 'five', 'six']
mylist+anotherlist
newlist = mylist + anotherlist
newlist

#We can also mutate in list
newlist[0] = 'ONE'
newlist

#We can use append in list which helps us to add (APPEND)a item in th end of a list.
newlist.append('seven')
newlist

#We can also remove items from the list for which we use (POP) method which basically pops out the item from the end of the list.
newlist.pop()
newlist

#We can also remove the items in list from in between
newlist.pop(0)
newlist

#We can also SORT list 
another_list = ['b', 'e', 'a', 'd', 'f', 'c', 'h', 'g', 'k', 'i', 'j']
another_list.sort()
another_list

#Trying sorting with the numbers
numlist = [10,8,6,4,2,9,7,5,3,1]
numlist.sort()
numlist

#We can also REVERSE the list 
numlist.reverse() 
numlist

#DICTIONARIES
#Dictionaries are unordered mappings for storing the objects. Dictionaries use key value pairing instead. 
#This key value pair allows user to quickly grab objects without needing to know an index location. 
#Dictionary uses urly braces and colon to signify the keys and their associated values.
#DICTIONARIES - objects retrieved by key name. They are unordered an connot be sorted.
#LIST - objects retrieved by location. Ordered sequence can be indexed or sliced.

mydict = {'key1':'value1','key2':'value2'}
mydict

mydict['key1']

prices = {'Apple':4.50,'Oranges':1.45,'Mango':5.66,'Banana':1.2}
prices['Apple']
prices['Banana']
prices['Oranges']