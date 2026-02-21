#Objects and Data Structures Assesment Test

#Number - They store numerical information in two form INTEGERS(whole numbers) and Floating Point(decimal points)
#Strings - Strings are the ordered sequence of characters
#Lists - They are mutable ordered sequence of objects
#Tuples - They are immutable ordered sequence of objects 
#Dictionary - They are the key value pairings which are unordered

#NUMBERS
#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
(100*2)/5+70-9.75

#Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5)
4*(6+5)

#What is the value of the expression 4 * 6 + 5 
4*6+5

#What is the value of the expression 4 + 6 * 5
4+6*5

#What is the type of the result of the expression 3 + 1.5 + 4?
type(3 + 1.5 + 4)

#What would you use to find a number’s square root, as well as its square?
#square root
100 ** 0.5
#Square
10 ** 2

#STRINGS

#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
s[1]

#Reverse the string 'hello' using slicing:
s = 'hello'
s[::-1]

#Given the string hello, give two methods of producing the letter 'o' using indexing.
s = 'hello'
s[4]
s[4:]
s[-1]

#LISTS
#Build this list [0,0,0] two separate ways.
#Method 1
[0]*3
#Method 2
list = [0,0,0]
list

#Reassign 'hello' in this nested list to say 'goodbye' instead:
list = [1,2,[3,4,'hello']]
list[2]
list[2][2]
list[2][2] = 'goodbye'
list

#Sort the list below:
list1 = [5,3,4,6,1]
list1.sort()
list1

#DICTIONARIES
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
d['simple_key']

d = {'k1':{'k2':'hello'}}
d['k1']
d['k1']['k2']

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d['k1'][0]['nest_key'][1]

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d['k1'][2]['k2'][1]['tough'][2]

#TUPLES
#What is the major difference between tuples and lists?
#Tuples are immutable and lists are mutable.

#How do you create a tuple?
t = (1,2,3)
type(t)

#SETS
#What is unique about a set?
#Sets are unordered collections of unique elements, like A cannot there more than one time.

#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)

#BOOLEANS
#What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
2 > 3 #False

3 <= 2 #False

3 == 2.0 #False

3.0 == 3 #True

4**0.5 != 2 #False

#Final Question: What is the boolean output of the cell block below?
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

l_one[2][0] >= l_two[2]['k1'] #False 