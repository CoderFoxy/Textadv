#!/usr/bin/env python3
INVENTORY = []

name = input("Unknown Voice: What's your name, stranger? ") #stranger

print(f"Unknown Voice: Hello, {name}. Welcome to The Flaming Empire, an isolated, fantasy realm located in a secret place.") #stranger


def room_greeting():
    print("Unknown Voice: But that isn't important right now. I have a mission for you; a quest. Are you up for the task? A yes or no answer would be useful...no maybes.") #stranger
    command = input("~ ").lower()
    if command == "yes":
        print("Unknown Voice: Great! Let me retrieve your resources you will need for the journey. For now, explore around!") #stranger
        room_start()
    elif command == "no":
        print("Unknown Voice: Well, too bad. You'll be fine. I won't take no as an answer. I'll go get your things.") #stranger
        room_start()
    else:
        print("INVALID COMMAND! Try again.") #computer
        room_greeting()

room_exit2_took_key = False
def room_exit2():
    global room_exit2_took_key
    print("You look around and spot something shiny under a broken, three-legged chair. Would you like to take it?")
    command = input("~ ").lower()
    if command == "yes" and not room_exit2_took_key:
        print("It's a key. Maybe it unlocks something? Perhaps the door...")
        room_exit2_took_key = True
        INVENTORY.append('key')
        room_start()
        #print("You put the key in the handle and turn it. It works! A long corridor meets your eyes. Would you like to proceed?")
        #if command == "yes":
                #room_corridor()
    #if command == "no":
    #    print("There is no where else to go, {name}. We'll guide you in the right direction.")
    #    room_corridor()

def room_exit():
    global room_exit2_took_key
    print("You try opening the door. It's locked. There must be a key somewhere...")
    print("Where would you like to look? There's a chair, a cabinet, and a bookshelf.")
    command = input("~ the ").lower()
    if command == "chair":
        print("You find the key!")
        room_exit2_took_key = True
        INVENTORY.append('key')
        room_start()
    elif command == "cabinet":
        print("Nothing here except some lint...look again.")
        room_exit()
    elif command == "bookshelf":
        print("Nothing here, sorry. Try somewhere else.")
        room_exit()
    else:
        print("INVALID COMMAND! Try again.")

def room_start():
    if "key" in INVENTORY:
        room_corridor()
    else:
        print("You are in an empty room with firm stone walls, some dusty furniture, no windows, and a door. Would you like to exit?")
        command = input("~ ").lower()
        if command == "yes":
            room_exit()
        elif command == "no":
            room_exit2()

def room_corridor():
    pass

room_greeting()
