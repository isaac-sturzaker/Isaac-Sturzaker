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

    #prints go after countdown has done
    if num == 0:
        print("GO!")
        time.sleep(.600)

def gamble_question(points):
    """Function that has gambilng code in it"""

    #Random and Time Library
    import random
    import time
    
    print("\n---------------------------------------------------------------")
    #Prints the users points
    print("\nCalculating Score")
    print("\nYour Points: {}".format(points))

    #Game rules
    print("""\nIn this you will gamble your points, you will then choose a random number between 1 and 5,
if we guess the same number then the points you have chosen to gamble will double, if we guess different
numbers then you will lose those points
""")
    repeat = True
    while repeat:
        #Ask user how many points to gamble
        users_points = int(input("How many points would you like to gamble: "))

        if user_points > points:
            print("You do not have enough points")
            repeat = True

        elif user_points <= 0:
            print("You need to gamble something")
            repeat = True

        else:
            print("Lets Begin")
            repeat = False

        repeat = True
        while repeat:
            #Random number between 1 and 5
            random_num = random.randint(1, 5)
               
            #Users Number
            user_num = int(input("Please choose a number between 1 and 5"))
            if user_num > 5 or user_num < 1:
                print("Please a number between 1 and 5")
                repeat = True

            if user_num == random_num:
                print("Congratulations")
          
                           
        
def gamble_func(rounds, points):
    """Asks the user if they would like to gamble their points"""

    import time

    repeat = True
    while repeat:
        print("\n---------------------------------------------------------------")
        user_choice = input("""\nWould you be interested in gambling your points?\n (Y)Yes\Ae\n (N)No\Kore kau\n (H)Whats Gambling\n """).lower()
       
        if user_choice == "y" or user_choice == "yes":
            if points == 0:  #Checks if user has any points
                print("\n---------------------------------------------------------------\n")
                print("Sorry you do not have any points \nPlease continue to play to earn points")
            else:
                print("\nTransfering...")
                time.sleep(2)
                repeat = False
                gamble_question(points)
            

        elif user_choice == "n" or user_choice == "no":
            print("\nOK!")
            repeat = False

        #If the user picks the "Whats Gambling?" Then it will take them to the help function
        elif user_choice == "h":
            print("\nTransfering...")
            time.sleep(2)
            help_func()
            repeat = True #After the user goes to the help function it will bring them back and ask them again
                    

        else:
            print("Please pick a valid input")
            repeat = True
            
            
    

def help_func():
    """Gives information about the different game modes"""
    print("\n---------------------------------------------------------------\n")
    help_mode = input("""\nWhich mode would you like to learn about:\n \n(1)Classic\Panui\n \n(2)Arcade\n \n(3)Gambling\Petipeti\n \n(4)Return\Hoki\n""")
    
    

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
    import time

    #The number of questions there will be each round
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
        print("---------------------------------------------------------------\n")
        start = input("Press S to start: ").lower()
        
        if start == "s":
            repeat = False
        else:
            print("Please enter a valid input\n")

    #Starting the countdown
    count_down()

    for i in range(10):
        #Sets Random number between 0 and 10 for variable  
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operator = random.choice(operations) 
        
        #Generating correct answer and prints question
        real_answer = eval(str(num1) + operator + str(num2))
        user_answer = int(input("\n{} {} {} = ".format(num1, operator, num2))) # - Prints out the question
        
        #If the answer is correct then add points
        if user_answer == real_answer:
            points += 125

        #If the user answer is null or letters it will count as incorrect
        elif user_answer == None:
            print("Even if you dont know the answer, give it a go!")
            correct -= 1
            
        else:
            correct -= 1
            
                
    print("\n---------------------------------------------------------------")
    #Prints the users points
    print("\nCalculating Score")
    time.sleep(2)
    print("\nYour Points: {}".format(points))
    print("Questions Correct: {}/10".format(correct))
    rounds -= 1
    gamble_func(rounds, points) #Calls gambling function

    
    
            

def main():
    """This is the main funtion which is going to
       ask the user which game mode they would like to play and
       then take them to that mode
    """

    #This will hold points lives and operators
    operations = ["+", "-", "*"]
    points = 0
    lives = 3 #During the arcade
    rounds = 5 #The user can only play a certain amount of rounds before they have to stop
    
    repeat = True #Repeat question untill valid answer is input
    while True:
        print("\n---------------------------------------------------------------")
        #Asking the user which mode they would like to play
        game_mode = input("\nPlease choose a game mode\n \n(1)Classic\Panui\n \n(2)Arcade\Taarua\n \n(3)Help\Awhina\n \n(4)Exit\Puta\n").lower().strip()

        #If statement that takes user to function dependet on the mode they chose
        if game_mode == "1" or game_mode == "classic" or game_mode == "panui":
            classic_func(rounds, points, operations)
            repeat = False
            
        elif game_mode == "2" or game_mode == "arcade" or game_mode == "taarua":
            arcade_func(rounds, points, lives, operations)
            repeat = False

        elif game_mode == "3" or game_mode == "help" or game_mode == "awhina":
            help_func()
            repeat = False

        elif game_mode == "4" or game_mode == exit or game_mode == "puta":
            print("Thanks for playing!")
            exit()

        else:
            print("\nPlease input a valid mode")
        

main()

