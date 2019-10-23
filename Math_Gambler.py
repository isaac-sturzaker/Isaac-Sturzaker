#Assessment: Math Gambler
#Author: Isaac Sturzaker
#Date Started: 23/07/19

import sys
try: color = sys.stdout.shell
except AttributeError:
    print("Please use IDLE!")


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
        color.write("GO!\n","KEYWORD")
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

        if users_points > points:
            print("\nYou do not have enough points")
            repeat = True

        elif users_points <= 0:
            print("\nYou need to gamble something")
            repeat = True

        else:
            print("\nLets Begin")
            repeat = False

    repeat = True
    while repeat:
        #Random number between 1 and 5
        random_num = random.randint(1, 5)
           
        #Users Number
        print("\n---------------------------------------------------------------")
        user_num = int(input("Please choose a number between 1 and 5"))
        if user_num > 5 or user_num < 1:
            print("Please choose a number between 1 and 5; ")
            repeat = True
        print(random_num)
        if user_num == random_num:
            repeat = False
            print("Congratulations")
            print("+{} points".format(users_points))
            points += users_points

        elif user_num != random_num:
            repeat = False
            print("Unlucky, u lost")
            print("-{} points".format(users_points))
            points -= users_points

    

            
          
                           
        
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

    import time
        
    repeat = True
    while repeat:
        print("\n---------------------------------------------------------------\n")
        help_mode = input("""\nWhich mode would you like to learn about:\n \n(1)Classic\Panui\n \n(2)Arcade\n \n(3)Gambling\Petipeti\n \n(4)Return\Hoki\n""")

        #Will explain the mode
        if help_mode == "4":
            repeat = False
            print("\nTransfering...")
            time.sleep(2)
            #If i leave blank then it will automatically send user back to function they called from
            print("\n")


        elif help_mode == "1":
            print("""\nEnglish: In this game mode you will be given 10 hard questions.
    Each question rewards you with a set amount of points.
    If you get a question wrong the game will stop and you will
    lose all your points​.""" )
            print("""\nMaori: I tenei aratau kēmu ka tukuna kia 10 nga patai uaua.
    Ma ia patai te utu ki a koe me te nui o nga whaainga.
    Ki te whiwhi koe i tetahi patai hē ka mutu te kēmu ka mutu koe
    ngaro koutou tohu katoa.""")
            time.sleep(2)

        elif help_mode == "2":
            print("""\nEnglish: In this game mode you will be given 10 questions
    while being timed. You then need to answer all the questions, CORRECTLY, ​
    in order to stop the timer. You will then be awarded points dependant on the
    time you got.""")
            print("""\nMaori: 
    I tenei aratau kēmu ka tukuna kia 10 nga patai
    i te wātaka. Me whakautu e koe nga whakautu katoa, tika
    kia mutu ai te taima. Ka whakawhiwhia koe ki nga tohu i runga i te
    wa kua ka koe""")
            time.sleep(2)

        elif help_mode == "3":
            print("""\nEnglish: In this gambling game you will choose how many
    you would like to gamble. The game wil then ask you to pick a number
    between 1 and 5. If you get the number right you will get your points
    doubled. If you get this wrong you will lose thos points you gambled.""")
            print("""\nMaori: 
    I tenei kēmu petipeti ka whiriwhiri koe kia hia
    pai ki te petipeti koe. Ka kii atu koe ki te tiki i te nama
    i waenga i te 1 me te 5. Mena ka whiwhihia e koe te whika ka riro koe i ou tohu
    takirua. Mena ka he koe i tenei he ka ngaro nga tohu a koe i poipoihia e koe""")
            time.sleep(2)


def arcade_func(rounds, points, lives, operations):
    """Arcade Mode is a certan amount of time with rapid fire questions
       and each correct answer gives you a set amount of points
    """

    import time
    import random

    print("\n---------------------------------------------------------------") 

    print("\nArcade\Taarua\n")

    #Describing the game mode
    print("""In this game mode you will be given 10 questions
while being timed. You then need to answer all the questions, CORRECTLY, ​
in order to stop the timer. You will then be awarded points dependant on the
time you got.
""")

    #Asking user if they want to start the game
    repeat = True
    while repeat:
        color.write("Press ENTER to start:","KEYWORD")
        start = input("").lower()
        
        if start == "":
            repeat = False
        else:
            print("\n")
            repeat = True

    #Starting the countdown
    count_down()

    #Question answered correctly and incorrectly along with with total 
    correct = 0
    incorrect = 0
    total = 0
    
    #This starts the timer
    start = time.time()

    for i in range(100):
        #Sets Random number between 0 and 10 for variable  
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operator = random.choice(operations) 
        
        #Generating correct answer and prints question
        real_answer = eval(str(num1) + operator + str(num2))
        user_answer = int(input("\n{} {} {} = ".format(num1, operator, num2))) # - Prints out the question
    

        #Going to calculate the average depending on the users time and give them points
        if user_answer == real_answer:
            points += 125
            correct += 1
            total += 1
            if correct > 10:
                finish = time.time()
                elapsed = finish - start
                break
                #print("{:.1f}".format(elapsed))
            
        else:
            incorrect += 1
            total += 1

    
    print("\n---------------------------------------------------------------")
    #Prints the users points
    print("\nCalculating Score")
    time.sleep(2)
    print("\nYour Points: {}".format(points))
    print("Total Time: {:.1f} seconds".format(elapsed))
    rounds -= 1
    gamble_func(rounds, points) #Calls gambling function
        

def classic_func(rounds, points, operations):
    """Classic Mode is a certan amount of questions
       and each correct answer gives you a set amount of points
    """

    #Imports random library then chooses two random numbers and a random operator
    import random
    import time

    #The number of questions there will be each round
    correct = 10

    print("\n---------------------------------------------------------------") 
    
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
        color.write("Press ENTER to start:","KEYWORD")
        start = input("").lower()
        
        if start == "":
            repeat = False
        else:
            print("\n")
            repeat = True

    #Starting the countdown
    count_down()

    for i in range(10):
        #Sets Random number between 0 and 10 for variable  
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operator = random.choice(operations) 
        
        #Generating correct answer and prints question
        real_answer = eval(str(num1) + operator + str(num2))
        repeat_quest = True
        
            
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

    
def menu(points, lives, operations, rounds):
    """This is the menu funtion which is going to
       ask the user which game mode they would like to play and
       then take them to that mode"""
    

    import time

    if rounds == 0:
        print("""I am sorry but you have reached the
maximum amount of rounds and it is unthealthy for you
to continue. Please play again another time!""")
        exit()
    
    repeat = True #Repeat question untill valid answer is input
    while True:
        print("\n---------------------------------------------------------------")
        #Asking the user which mode they would like to play
        
        game_mode = input("\nPlease choose a game mode\n \n(1)Classic\Panui\n \n(2)Arcade\Taarua\n \n(3)Help\Awhina\n \n(4)Exit\Puta\n").lower().strip()

        #If statement that takes user to function dependet on the mode they chose
        if game_mode == "1" or game_mode == "classic" or game_mode == "panui":
            print("\nTransfering...")
            time.sleep(2)
            points = classic_func(rounds, points, operations)
            repeat = True
            
        elif game_mode == "2" or game_mode == "arcade" or game_mode == "taarua":
            print("\nTransfering...")
            time.sleep(2)
            arcade_func(rounds, points, lives, operations)
            repeat = True

        elif game_mode == "3" or game_mode == "help" or game_mode == "awhina":
            print("\nTransfering...")
            time.sleep(2)
            help_func()
            repeat = True

        elif game_mode == "4" or game_mode == exit or game_mode == "puta":
            print("Thanks for playing!")
            exit()

        else:
            print("\nPlease input a valid mode")
            

def main():
    """This is the main funtion which holds variables"""

    import time
    #This will hold points lives and operators
    operations = ["+", "-", "*"]


    points = 0 
    lives = 3 #During the arcade
    rounds = 5 #The user can only play a certain amount of rounds before they have to stop
    
    menu(points, lives, operations, rounds)
    
   

    
     

main()

