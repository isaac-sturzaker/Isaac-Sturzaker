#Assessment: Math Gambler
#Author: Isaac Sturzaker
#Date Started: 23/07/19

def classic_func():
    """Classic Mode is a certan amount of questions
       and each correct answer gives you a set amount of points
    """

    

    #Imports the time library
    import time 

    #A countdown to start the mode
    num = 3 
    for i in range(3):
        print("{}...".format(num))
        num -= 1
        for i in range(1):
            time.sleep(1)
            

def main():
    """This is the main funtion which is going to
       ask the user which game mode they would like to play and
       then take them to that mode
    """

    repeat = True #Repeat question untill valid answer is input
    while True:
        #Asking the user which mode they would like to play
        game_mode = input("\nPlease choose a game mode\n (C)Classic\Panui\n (A)Arcade\n (H)Help\Awhina \n").lower().strip()

        #If statement that takes user to function dependet on the mode they chose
        if game_mode == "c":
            classc_func()
            repeat = False
            
        elif game_mode == "a":
            arcade_func()
            repeat = False

        elif game_mode == "h":
            help_func()
            repeat = False

        else:
            print("\nPlease input a valid mode")
        

main()

