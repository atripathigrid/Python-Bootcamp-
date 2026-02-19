#CHALLENGING PROBLEMS

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(num):
    code = [0,0,7,'x']
    for num in num:
        if num == code[0]:
            code.pop()
    return len(code) == 1
spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])


#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.
def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
count_primes(100)


#Just for fun, not a real problem :)
#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
#print_big('a')
#out:   *  
#      * *
#     *****
#     *   *
#     *   *
#HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
#For purposes of this exercise, it's ok if your dictionary stops at "E".
def print_big(letter):
    patterns = {1:'  *  ',2:'*   * ',3:'*   *',4:'*****',5:'**** ',6:'  * ',7:' *  ',8:'*  *',9:'*   '}
    alphabets = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabets[letter.upper()]:
        print(patterns[pattern])
print_big('a')
print_big('c')
print_big('d')





