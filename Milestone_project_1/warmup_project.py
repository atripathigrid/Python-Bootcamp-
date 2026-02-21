#FUNCTION TO DISPLAY INFORMATION

#Creating a function that displays a list for the user
def display_list(mylist):
    print(mylist)
mylist = [0,1,2,3,4,5,6,7,8,9,10]
display_list(mylist)


#ACCEPTING USER INPUT 

#Creating function that takes in an input from user and returns the result in the correct data type. Be careful when using the input() function, running that cell twice without providing an input value will cause python to get hung up waiting for the initial value on the first run. You will notice an In[*] next to the cell if it gets stuck, in which case, simply restart the kernel and re-run any necessary cells.
def user_choice():
    '''
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    '''
    choice = input("Please input a number (0-10)")
    
    return int(choice)
user_choice()
result = user_choice()
result
type(result)


#VALIDATING USEER INPUT

#** Check that input is valid before attempting to convert.**
#We'll use a simple method here.
#As you get more advanced, you can start looking at other ways of doing this (these methods will make more sense later on in the course, so don't worry about them for now).
some_input = '10'
some_input.isdigit()

#** Edit the function to confirm against an acceptable value or type **
def user_choice():
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Choose a number: ")
    return int(choice)
user_choice()

#Let's try adding an error message within the while loop!
def user_choice():
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Choose a number: ")
        if choice.isdigit() == False:
            print("Sorry, but you did not enter an integer. Please try again.")
    return int(choice)
user_choice()

#SIMPLE USER INTERACTION

#Finally let's combine all of these ideas to create a small game where a user can choose a "position" in an existing list and replace it with a value of their choice.
game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list")
    print(game_list)
display_game(game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position to replace (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry, but you did not choose a valid position (0,1,2)")
    return int(choice)
position_choice()

def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at the position: ")
    game_list[position] = user_placement
    return game_list
replacement_choice(game_list,1)

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("Would you like to keep playing? Y or N ")
        if choice not in ['Y','N']:
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
    if choice == "Y":
        return True
    else:
        return False
gameon_choice()
    
#Game Logic All Together

game_on = True
game_list = [0,1,2]
while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()
