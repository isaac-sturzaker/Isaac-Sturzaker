#Assessment: Math Gambler
#Author: Isaac Sturzaker
#Date Started: 23/07/19
def count_down():
    """Gives the countdown to start the game"""

    #Imports the time library
    import time

    #A countdown to start the mode
    num = 3 
    for i in range(3):
        print("{}...".format(num))
        num -= 1
        time.sleep(1)

    if num == 0:
        print("GO!")
        time.sleep(1)

def help_func():
    """Gives information about the different game modes"""
    help_mode = input("Which mode would you like to learn about:\n (C)Classic\Panui\n (A)Arcade\n (R)Return\Hoki\n")
    
    

def arcade_func(rounds, points, lives, operations):
    """Arcade Mode is a certan amount of time with rapid fire questions
       and each correct answer gives you a set amount of points
    """

    print("\nArcade")

    #Describing the game mode
    print("""In this game mode you will be given a set of time (30 seconds.
It will be a rapid fire game and the user will have to answer as many
question in the time frame. Each question giving the user a set amount of points.​
""")

    #Asking user if they want to start the game
    repeat = True
    while repeat:
        start = input("Press S to start: ").lower()
        
        if start == "s":
            repeat = False
        else:
            print("Please enter a valid input\n")

    #Starting the countdown
    count_down()

    print("\nIt Works")
        

def classic_func(rounds, points, operations):
    """Classic Mode is a certan amount of questions
       and each correct answer gives you a set amount of points
    """

    #Imports random library then chooses two random numbers and a random operator
    import random

    #The number of questions there will be each round
    question = 10
    correct = 10
    
    
    print("\nClassic\Panui\n")

    #Describing the game mode
    print("""In this game mode you will be given 10 hard questions.
Each question rewards you with a set amount of points.
If you get a question wrong the game will stop and you will
lose all your points​.
""")

    #Asking user if they want to start the game
    repeat = True
    while repeat:
        start = input("Press S to start: ").lower()
        
        if start == "s":
            repeat = False
        else:
            print("Please enter a valid input\n")

    #Starting the countdown
    count_down()

    repeat = True
    while repeat:
        #Random number between 0 and 10 for the questions
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)

        #Randomly chooses a math operator
        operator = random.choice(operations)

        user_answer = int(input("\n{} {} {} = ".format(num1, operator, num2))) # - Prints out the question
        real_answer = eval(str(num1) + operator + str(num2)) # - Turns the string question into integers
                                                             #   and stores the answer is a variable

        
        question -= 1 #Changes question number 
        if user_answer == real_answer:
            points += 125
            if question == 0:
                repeat = False

                
                
                   
                
        else:
            correct -= 1
            
    print("\nYour Points: {}".format(points))
    print("Questions Correct: {}/10".format(correct))
    rounds -= 1
            
            
    
        
        
    
    
    
    

def main():
    """This is the main funtion which is going to
       ask the user which game mode they would like to play and
       then take them to that mode
    """

    #This will hold points lives and operators
    operations = ["+", "-", "*"]
    points = 0
    lives = 3
    rounds = 5
    
    repeat = True #Repeat question untill valid answer is input
    while True:
        #Asking the user which mode they would like to play
        game_mode = input("\nPlease choose a game mode\n (C)Classic\Panui\n (A)Arcade\n (H)Help\Awhina\n (E)Exit\Puta\n").lower().strip()

        #If statement that takes user to function dependet on the mode they chose
        if game_mode == "c":
            classic_func(rounds, points, operations)
            repeat = False
            
        elif game_mode == "a":
            arcade_func(rounds, points, lives, operations)
            repeat = False

        elif game_mode == "h":
            help_func()
            repeat = False

        elif game_mode == "e":
            print("Thanks for playing!")
            exit()

        else:
            print("\nPlease input a valid mode")
        

main()

