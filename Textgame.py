########
#Title: Touch the orb
#You start off in a room with four doors. You have to explore and find the key to open the door to go down the stairs and touch the orb
#Your final goal is to touch the orb
#Global Variable: haveKey
#This is how you can open the door to go down the stairs, but you have to find the key first. 
########
#SPOILERS
#there are multiple locations to find the key, the beds room after choosing option 'nap' and others are when you talk to the fish and choose either 'do a little dance' or 'bribe him' 
#once you get the key you can open the door and go down the staircase
#you can also skip everything by going to the library and choosing the option pick up a book
#once you touch the orb you explode and win the game
########
#import modules
#######
import os
########
#define functions
#######
def start():
    print("Welcome!")
    main_room()

def main_room():
    print("You are in the main room.")
    move = input("\nWhich room would you like to go into? Say one of these choices:\n\ta)office\n\tb)staircase\n\tc)hallway\n\td)animal room\n")
    if move.lower() == "a":
        os.system('clear')
        office()
    elif move.lower() == "b":
        os.system('clear')
        staircase()
    elif move.lower() == "c":
        os.system('clear')
        hallway()
    elif move.lower() == "d":
        os.system('clear')
        zoo_place()
    else:
        whatelse(main_room)

#room office
def office():
    print("You are in the office")
    move = input("\nWhat would you like to do? Say one of these choices:\n\ta)leave the room\n\tb)look around\n")
    if move.lower() == "a":
        os.system('clear')
        main_room()
    elif move.lower() == "b":
        os.system('clear')
        print("You shuffle through papers and drawers. Nothing seems that important.\n")
        office()
    else:
        whatelse(office)

#room staircase and all of the attachments
def staircase():
    os.system('clear')
    global haveKey
    #change this because it is the staircase
    if haveKey == True : 
        print("You slide the key into the lock and turn. The door swings open easily.")
        move = input("\nWhere would you like to go? Say one of these choices:\n\ta) leave the doorway\n\tb)down the stairs\n")
        if move.lower() == "a":
            os.system('clear')
            main_room()
        elif move.lower() == "b":
            os.system('clear')
            staircase_actual()
        else:
            whatelse(staircase)
    
    if haveKey == False :
        print("You try to open the door to the staircase...\nIt's locked.\nMaybe you should find a key\n")
        main_room()

def staircase_actual():
    stair_go = input("The stairs are dimly lit and seem to go on forever.\n\nContinue?\n\ta)yes\n\tb)no\n")
    if stair_go == 'a' :
        os.system('clear')
        orb_room()
    if stair_go == 'b' :
        os.system('clear')
        print("You head back up to the main room")
        main_room()

def orb_room():
    touch_orb = input("You find yourself in a strange room. In the middle there is a pedestal with a glowing blue orb.\nTouch the orb?\n\ta)yes\n\tb)no\n")
    if touch_orb == 'jfndsf':
        os.system('clear')
        print("you explode\n\nGame over")
        play_again()
    else: 
        os.system('clear')
        print("you explode\n\nCongrats!")
        play_again()
    

#room animal room and all of its attatchments
def zoo_place():
    os.system('clear')
    print("You are in a room filled with animals")
    move = input("\nWhat would you like to do? Say one of these choices:\n\ta)leave the room\n\tb)talk to the fish\n")
    if move.lower() == "a":
        os.system('clear')
        main_room()
    elif move.lower() == "b":
        fish()
    else:
        whatelse(zoo_place)

def fish():
    global haveKey

    os.system('clear')
    print("You stare at the small goldfish\nThere appears to be a key in his mouth\n")
    fish_answer = input("What would you like to do?\n\ta)tap on the glass\n\tb)do a little dance\n\tc)bribe him\n")

    if fish_answer == 'a':
        os.system('clear')
        print("He swims away with the key, never to be seen again\n\nGame Over")
        play_again()

    
    elif fish_answer == 'b':
        os.system('clear')
        print("He seems as though he is laughing at you. He drops the key and swims away. You reach your hand in and grab the key.")
        haveKey = True
        repp = input("\nYou seem about done in here. Leave?\na)yes\tb)no\n")
        if repp == 'a':
            os.system('clear')
            start()
        else:
            zoo_place()

    elif fish_answer == 'c':
        os.system('clear')
        print("He seems pleased. He drops the key and swims away. You reach your hand in and grab the key.")
        haveKey = True
        repp = input("\nYou seem about done in here. Leave?\na)yes\tb)no\n")
        if repp == 'a':
            os.system('clear')
            start()
        else:
            zoo_place()

    else:
        whatelse(fish)

    
#room hallway 
def hallway():
    os.system('clear')
    print("You are in the hallway")
    move = input("\nWhere would you like to go? Say one of these choices:\n\ta)main room\n\tb)beds room\n\tc)library\n")
    if move.lower() == "a":
        os.system('clear')
        main_room()
    elif move.lower() == "b":
        os.system('clear')
        beds_room()
    elif move.lower() == "c":
        os.system('clear')
        library()
    else:
        whatelse(hallway)

#room beds room
def beds_room():
    global haveKey
    print("You are in a room filled with beds")
    move = input("\nWhat would you like to do? Say one of these choices:\n\ta)leave the room\n\tb)nap\n")
    if move.lower() == "a":
        os.system('clear')
        hallway()
    elif move.lower() == "b":
        os.system('clear')
        print("You lie down for a small nap but find a key under the pillow.You grab it.\n")
        haveKey = True
        beds_room()
    else:
        whatelse(beds_room)

#room library
def library():
    print("You are in a library")
    move = input("\nWhat would you like to do? Say one of these choices:\n\ta)leave the room\n\tb)look around\n\tc)pick up a book\n")
    if move.lower() == "a":
        hallway()
    elif move.lower() == "b":
        os.system('clear')
        print("You scan the bookshelves. Nothing seems to appeal to you.\n")
        library()
    elif move.lower() == "c":
        os.system('clear')
        print("You try to pick up a book off of the shelves, instead, a trap door opens and you slide down a tunnel.\n")
        orb_room()
    else:
        whatelse(library)

#this is for when the computer doesn't know what that person typed
def whatelse(x):
    os.system('clear')
    repp = input("\n\nNot sure what you said... try again?\na)yes\tb)no\n")
    if repp == 'a':
        x()
    else:
        os.system('clear')
        print("\nGame Over")
        play_again()

#play again?
def play_again():
    again = input("\nPlay again?\n\ta)yes\n\tb)no\n")
    if again == 'a':
        os.system('clear')
        start()
    if again == 'b':
        os.system('clear')
        print("Goodbye")
########
#main
#######
#TODO: Add some global variables

haveKey = False

start()