#def keyword
def say_hello():
    print('Hello')
say_hello

def say_hello():
    print('Hello')
    print('Its')
    print('me')
say_hello()

def even_check(number):
    result = number % 2 == 0
    return result

even_check(20)
even_check(21)

#Return true if any number is even inside the list

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

check_even_list([1,3,4,5])
check_even_list([1,3,5,7])
check_even_list([2,4,6,8,10])
check_even_list([2,4,5])


def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            return False #Wrong!!!!!

check_even_list([1,3,4,5])
check_even_list([1,3,5,7])
check_even_list([2,4,6,8,10])
check_even_list([2,4,5])


def check_even_list(num_list):
    #return all the even numbers in a list

    #placeholders variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)

        else:
            pass
    return even_numbers

check_even_list([1,3,4,5])
check_even_list([1,3,5,7])
check_even_list([2,4,6,8,10])
check_even_list([2,4,5])



#Tuples unpacking wth python funtions
stock_prices = [('Apple',2000),('Google',1000),('Netflix',1500),('Samsung',2500),('Adobe',800)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(ticker)


stock_prices = [('Apple',2000),('Google',1000),('Netflix',1500),('Samsung',2500),('Adobe',800)]
for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(price)


#Working on working hours 
work_hours = [('Aman',150),('Shubham',90),('Prashant',350),('Deepak',260)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours 
            employee_of_month = employee 
        else:
            pass


    #Return
    return(employee_of_month,current_max)

employee_check(work_hours)


#Interactions between python Functions
from random import shuffle
mylist = ['','o','']
shuffle(mylist)
mylist

def player_guess():
    guess=''

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1, or 2")

    return int(guess)

player_guess()

myindex = player_guess()
myindex

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(mylist)

#Intial List
mylist = ['','o','']

#Shuffle List
from random import shuffle
mixedup_list = shuffle(mylist)
mylist

#User Guess
guess = player_guess()

#Check Guess
check_guess(mixedup_list,guess)
