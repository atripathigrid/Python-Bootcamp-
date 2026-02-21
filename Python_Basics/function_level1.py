#FUNCTION LEVEL1 PROBLEMS

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'
old_macdonald('macdonald')


#MASTER YODA: Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'
def master_yoda(text):
    return ' '.join(text.split()[::-1])
master_yoda('I am home')
master_yoda('We are ready')


#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True
#NOTE: abs(num) returns the absolute value of a number
def almost_there(n):
    return ((abs(100-n) <= 10) or (abs(200-n) <= 20))
almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)


