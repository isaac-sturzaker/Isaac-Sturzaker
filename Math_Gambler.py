#Assessment: Math Gambler
#Author: Isaac Sturzaker
#Date Started: 23/07/19




def main():
    """This is the main funtion which is going to
       ask the user which game mode they would like to play and
       then take them to that mode
    """

    repeat = True #Repeat question untill valid answer is input
    while True:
        #Asking the user which mode they would like to play
        game_mode = input("\nPlease choose a game mode\n (C)Classic\n (A)Arcade\n (H)Help \n").lower().strip()

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

