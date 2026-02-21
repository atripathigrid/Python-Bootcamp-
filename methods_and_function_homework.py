#FUNCTIONS AND METHODS

#Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4/3)*(3.14)*(rad**3)
vol(2)


#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('he number is outside the range')
ran_check(5,2,7)


#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String :", s)
    print("No. of Upper case characters :", d["upper"])
    print("No. of Lower case characters :", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
        

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


#Write a Python function to multiply all the numbers in a list.
#Sample List : [1, 2, 3, -4]
#Expected Output : -24
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
multiply([1, 2, 3, -4])


#Write a Python function that checks whether a word or phrase is palindrome or not.
#A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"
def palindrome(s):
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''.
    return s == s[::-1]
palindrome('nurses run')


#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#Pangrams are words or sentences containing every letter of the alphabet at least once.
import string

def ispangram(str1, alphabet=string.ascii_lowercase): 
    # Create a set of the alphabet
    alphaset = set(alphabet)  
    
    # Remove spaces from str1
    str1 = str1.replace(" ",'')
    
    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation 
    str1 = str1.lower()
    
    # Grab all unique letters in the string as a set
    str1 = set(str1)
    
    # Now check that the alpahbet set is same as string set
    return str1 == alphaset
ispangram("The quick brown fox jumps over the lazy dog")
