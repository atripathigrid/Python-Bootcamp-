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






