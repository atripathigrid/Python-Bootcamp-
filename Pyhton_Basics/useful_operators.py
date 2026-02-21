#RANGE FUNCTION in python 
mylist = [1,2,3,4]
for num in range(10):
    print(num)

mylist = [1,2,3,4]
for num in range(4,10):
    print(num)
    
mylist = [1,2,3,4]
for num in range(0,10,2):
    print(num)

range(0,10,2)

list(range(0,10,2))

index_count = 0

for letter in 'abcdefgh':
    print('At index {} the letter {}' .format(index_count,letter))
    index_count += 1

#ENUMERATE FUNCTION
word = 'abcde'
for item in enumerate(word):
    print(item)

word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)

word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


#ZIP FUNCTION
mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c','d','e','f']
for item in zip(mylist1,mylist2):
    print(item)


mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c','d','e','f']
mylist3 = [10,20,30,40,50,60]
for item in zip(mylist1,mylist2,mylist3):
    print(item)


list(zip(mylist1,mylist2,mylist3))

#MATHEMATICAL FUNCTIONS
mylist = [100,200,300,400,500,600]
min(mylist)
max(mylist)

#RANDOM LIBRARIES
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
mylist

from random import randint
randint(0,50)

#INPUT FUNCTION 
input('Enter a number here:')

result = input('What is your name?')
result



#List Comprehensions
#List comprehensions are a unique way of quickly creating a list with python.
#Like if you find yourself using a for loop along with .append() create a list, List Comprehensions are a good altenative.

mylist = [x for x in 'word']
mylist

mylist = [letter for letter in 'hello']
mylist

mylist = [x for x in range(0,11) if x%2==0]
mylist

mylist = [x**2 for x in range(0,11) if x%2==0]
mylist


celcius = [0,5,10,20,25,35]
fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
fahrenheit

#NESTED LOOPS
mylist = []

for x in[2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

mylist