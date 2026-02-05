#PYTHON STATEMENTS
#IF, ELIF, ELSE statements

#Syntax of IF statement
#if some_condition:
    #execute your code

#Syntax of IF/ELSE statement
#if some_condition:
    #execute your code
#else:
    #do something else


#Syntax of IF/ELIF/ELSE statement
#if some_condition:
  #execute your code
#elif some_other_condition:
   #do something different
#else:
   #do something else

#IF statement
if True:
    print('Its True!')

hungry = True
if hungry:
    print('Feed Me')

#IF/ELSE Statement

hungry = False
if hungry: 
    print('Feed Me!')
else:
    print('I am not hungry')

loc = 'Bank'
if loc == 'Auto shop':
    print('Cars are cool')
else:
    print('I dont know much')

#IF/ELIF/ELSE Statement

loc = 'Store'
if loc == 'Auto shop':
    print('Cars are cool')
elif loc == 'Bank':
    print('Money is cool')
elif loc == 'Store':
    print('Welcome to the store')
else:
    print('I dont know much')


name ='Achintya'
if name == 'Achintya':
    print('Hello Achintya')
elif name == 'Prateek':
    print('Hello Prateek')
elif name == 'Junaid':
    print('Hello Junaid')
else:
    print('What is your name?')


name ='Junaid'
if name == 'Achintya':
    print('Hello Achintya')
elif name == 'Prateek':
    print('Hello Prateek')
elif name == 'Junaid':
    print('Hello Junaid')
else:
    print('What is your name?')


name ='Sarthak'
if name == 'Achintya':
    print('Hello Achintya')
elif name == 'Prateek':
    print('Hello Prateek')
elif name == 'Junaid':
    print('Hello Junaid')
else:
    print('What is your name?')


#FOR LOOP 
#Syntax for FOR LOOP
#my_iterable = [1,2,3]
#for item_name in my_iterable:
    #print(item name)

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print('Hello')

#Print only even numbers
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 == 0:
        print(num)

#Using IF/ELSE statement
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

#Printing outside the loop
list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

#Printing inside the loop
list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    print(list_sum)

#Using FOR LOOP in Dictionaries
d = {'k1':1,'k2':2,'k3':3}

for item in d:
    print(item)

d = {'k1':1,'k2':2,'k3':3}

for item in d.items():
    print(item)

#To print only values
d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(value)

#WHILE LOOPS
#Syntax of a WHILE LOOP
#while some_boolean_condition:
       #do something

#We can also use else statement if we want to us it or whenever it is needed.
#Syntax 
#while some_boolean_condition:
      #do something
#else:
      #do something different


x = 0
while x < 8:
    print(f'The current value of x is {x}')

    x += 1

#Using ELSE statement in while loop 
x = 0
while x < 8:
    print(f'The current value of x is {x}')

    x += 1
else:
    print('x is not less than 8')


#Three keywords that are useful in loop (BREAK, CONTINUE,PASS)
#Breaks - break out of current closest enclosing loop
#Continue - goes to the top of the closest enclosing loop
#Pass - does nothing at all

