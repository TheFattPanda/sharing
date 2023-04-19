import random, os, time
from inputimeout import inputimeout, TimeoutOccurred
import json
import datetime
JohanPhrases = ["Johan: They're probably off getting into some sort of trouble. I'll go them.",
                "Johan: If my friends are not in the tavern, then they're probably up to something devious. I'll try and find them.",
                "Johan: My companions? Oh, I'm sure they're causing chaos and mischief as we speak. I'll try and find them.",
                "Johan: They're either asleep, drunk, or causing a commotion somewhere. I'll try and find them.",
                "Johan: Knowing my friends, they're probably getting into trouble somewhere. I best go find them.",
                "Johan: I have no doubt my comrades are off causing chaos and mayhem. It's what we do best. I'll try and find them.",
                "Johan: If I were to hazard a guess, I'd say my friends are causing a ruckus somewhere. I'll try and find them.",
                "Johan:My friends and I have a way of finding trouble wherever we go. I'm sure they're up to something. I'll try and find them."]
JohanSneakPhrases = ["Johan: Watch out Captain!",
                     "Johan: Don't get spotted!",
                     "Johan: Duck!",
                     "Johan: Hide yourselves!",
                     "Johan: Don't get caught!",
                     "Johan: Look out!"]
game = {"progress": 0}
with open('save.txt', 'w') as file:
    file.write(json.dumps(game))
os.system('clear')
print(" ______________________________________________________")
print("|                                                      |")
print("|\033[1m" + "             Pirates of The Western World" + "\033[0;0m             |")
print("|                                                      |")
print("|                                                      |")
print("|                                                      |")
print("|                 Press Enter to Begin                 |")
print("|                                                      |")
print("|______________________________________________________|")
next = input("")
os.system('clear')
for char in "Use A and D to navigate the menu. Press enter after each A and D input to execute. Press enter again after selecting your option.\n":
    time.sleep(0.03)
    print(char, end = '', flush = True)
time.sleep(1)
print(" ____________________________________")
print("|                                    |")
print("|                                    |")
print("|\033[1m" + "    Pirates of The Western World" + "\033[0;0m    |")
print("|                                    |")
print("|     --------                       |")
print("|    |New Game|         Load Game    |")
print("|     --------                       |")
print("|____________________________________|")
menu = True
b = 0
while(menu == True):
    next = input('')
    if next == 'd':
        b = b + 1
        if(b > 1):
            b = b - 1
    if next == 'a':
        b = b - 1
        if(b < 0):
            b = b + 1
    if b == 0:
        os.system('clear')
        print(" ____________________________________")
        print("|                                    |")
        print("|                                    |")
        print("|\033[1m" + "    Pirates of The Western World" + "\033[0;0m    |")
        print("|                                    |")
        print("|     --------                       |")
        print("|    |New Game|        Load Game     |")
        print("|     --------                       |")
        print("|____________________________________|")
        game = 0 # If they choose new game, game will equal zero, so if game == 0: start new game
    if b == 1:
        os.system('clear')
        print(" ____________________________________")
        print("|                                    |")
        print("|                                    |")
        print("|\033[1m" + "    Pirates of The Western World" + "\033[0;0m    |")
        print("|                                    |")
        print("|                      ---------     |")
        print("|     New Game        |Load Game|    |")
        print("|                      ---------     |")
        print("|____________________________________|")
        game = 1 # If they choose load game, game will equal one, so if game == 1: load game you will have to print all their stats in a file
    if next == '':
        break
if game == 1:
    with open('save.txt', 'r') as file:
        data = json.load(file)
    progress = int(data['progress'])
elif game == 0 or progress == 0:
    os.system('clear')
    for char in "You are a pirate and are part of an organization called, Creed of Wolfheim.\nThe Creed of Wolfheim are having a conflict with another organization called the The Akatsuki of the Shadows.\nYour mission is to travel to Conomi a country, and assassinate the leader of The Akatsuki of the Shadows to stop the conflict.\nYou must be careful becasue the leader is known to have control of the land of Conomi, so you need to be stealthy.\nThe Creed of Wolfheim's main mission is to take away the Golden Staff of Eldagord from the leader of The Akatsuki of the Shadows.\nIt is an ancient artifact that holds great power, and there is a myth that it may be the key to the hidden gate that allows time travel.\nYou must be off to your journey now, Mr. Edward Kensmen.":
        time.sleep(0.025)
        print(char, end="", flush=True)
    time.sleep(3)
    os.system('clear')
    for char in "Time: 10:30 AM\nKenzuma Island\nOn the port, meeting with Johan to gather a crew.":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(3)
    os.system('clear')
    for char in "Johan: Oi Captain, I got some mates that work at the Tavarn.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(2)
    for char in "Type yes or no to choose a decision.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Do you want to bring them along?(yes or no)":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    print("\n")
    choice1 = input("Enter here: ")
    if choice1 == 'yes':
        os.system('clear')
        for char in "Alright, bring them over.\n":
            time.sleep(0.04)
            print(char, end="", flush=True)
        time.sleep(1)
        i = random.randint(0,7)
        for char in JohanPhrases[i]:
            time.sleep(0.05)
            print(char, end="", flush=True)
    if choice1 == 'no':
        print("\n")
        for char in "Johan: You know, my bunch couldn't really fall below your standards, I ought to go get em' right about.":
            time.sleep(0.04)
            print(char, end="", flush=True)
        time.sleep(1)
    os.system('clear')
    for char in "12:00 PM\nAfter gathering the crew together, Johan introduces you to Leroy, Will, and Juan\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Ah you-\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    for char in "Johan: Johan\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "You never fail to impress me.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.9)
    for char in "Will: Alright lets just sail already.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "We gotta gear our ship and men. Lets gather supplies from the enemy's warehouse at midnight.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    os.system('clear')
    for char in "12:45 AM\nAfter sneaking into the enemy's camp, you notice that the warehouse is heavily guarded.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Johan: Captain how should we handle this situation?\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Type the word in the parenthesis to choose option.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Do you want to sneak into the warehouse(sneak) or have a shootout(shootout)?\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    print('\n')
    choice2 = input("Enter here: ")
    if choice2 == 'sneak':
        os.system('clear')
        for char in "You and your crew try to sneak into the warehouse.":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        os.system('clear')
        i = random.randint(0,5)
        for char in JohanSneakPhrases[i]:
            time.sleep(0.07)
            print(char, end="", flush=True)
        time.sleep(0.9)
        for char in "\nQuick! When you see the green dot press enter to hide from the enemies!":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(0.1)


        os.system('clear')
        for char in "2:00 AM\nIn the warehouse\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Johan: Captain! Look at all this loot!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)



    if choice2 == 'shoutout':
        os.system('clear')
        for char in "You shoot 3 enemies and alarm the whole camp of your presence.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Enemy: Oi! Get em'!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Quick! Shoot the enemies!":
            time.sleep(0.05)
            print(char, end="", flush=True)
        for char in "\nPress enter when you see the green dot":
            time.sleep(0.05)
        for char in "
