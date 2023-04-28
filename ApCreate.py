import random, os, time
from inputimeout import inputimeout, TimeoutOccurred
import json
import datetime


def get_player_choice(prompt, choices):
    # Print out the prompt
    for char in prompt:
        time.sleep(0.03)
        print(char, end = '', flush = True)
    time.sleep(1)
    match = False
    p_input = ""
    # Get the player's choice
    while match == False:
        p_input = input("\nEnter your choice: ").strip('\n')
        # Check that the input is valid
        for choice in choices:
            if choice == p_input:
                match = True
                return p_input

def change_health(amount):
    playerHealth = 100
    playerHealth -= amount
    # Check if the player is dead
    print("Your Health: ", playerHealth)
    if playerHealth == 0:
        print("You have died. Game over")
        quit()

def combat_game():
    enemyHealth = 100
    dot = 0
    while enemyHealth > 0:
        for char in "\nQuick! When you see the green dot press enter to shoot the enemies!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for dot in range(0,13):
                print(Dot_game[dot])
                try:
                    player_input = inputimeout(prompt = "", timeout = 1.00)
                    if(player_input == ""):
                        break
                except Exception:
                    continue
        if(dot < 3 or dot == 11 or dot == 2 or dot == 13):
            print("You missed your shot, you lost some health")
            Dot_game.insert(2, "🔴") # Inserts a red dot BEFORE index 2
            change_health(20)
            time.sleep(2)
            os.system("clear")
        elif (dot < 5 and dot >3 or dot == 9 or dot == 10):
            print("Your shot injuried the enemy.")
            Dot_game.insert(4, "🟡") # Inserts a yellow dot BEFORE index 4
            enemyHealth -= 20
            print("Enemy Health: ",enemyHealth)
            time.sleep(2)
            os.system("clear")
        elif(dot < 8 and dot > 5):
            print("Nice shot, the enemy is down!")
            enemyHealth -= 100
            time.sleep(2)
            os.system("clear")
def sneak_game():
    for char in "\nQuick! Type in the letter to hide!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    i = random.randint(0,25)
    print("Type letter:", Sneak_game[i])

    try:
        player_input = inputimeout(prompt = "", timeout = 2.0)
        if(player_input == Sneak_game[i]):
            return True
        else:
            return False
    except Exception:
        return False

def big_maze():
    finish = False
    your_height= 1
    your_length =0
    os.system('clear')
    for char in "You need to complete this maze in order to pick lock the vault. Use the WASD keys in order to move. The dot (*) represents your pick lock. Good luck!":
        time.sleep(0.03)
        print(char, end = '', flush = True)
    time.sleep(1)
    os.system('clear')
    while(finish == False):
        os.system('clear')
        maze = [['█','█','█','█','█','█','█','█','█','█','█','█','█','█'],
            [' ',' ','█',' ',' ','█','█',' ',' ',' ',' ',' ',' ','█'],
            ['█',' ',' ',' ','█','█',' ',' ','█',' ','█','█',' ','█'],
            ['█','█','█',' ',' ',' ',' ','█','█',' ','█',' ',' ','█'],
            ['█','█','█',' ','█',' ',' ',' ','█',' ','█','█',' ','█'],
            ['█',' ',' ',' ','█',' ','█',' ','█','█','█',' ',' ','█'],
            ['█',' ','█','█','█',' ','█',' ',' ',' ','█','█',' ','█'],
            ['█',' ','█',' ',' ',' ','█','█','█',' ',' ','█',' ','█'],
            ['█',' ','█',' ','█','█','█','█','█','█',' ','█',' ','█'],
            ['█',' ','█',' ',' ','█',' ',' ',' ','█','█','█',' ','█'],
            ['█',' ','█','█',' ',' ',' ','█',' ',' ','█','█',' ','█'],
            ['█','█','█','█','█','█','█','█','█','█','█','█',' ','█']]
        for height in range(0,2+your_height):
            for length in range(0,2+your_length):
                maze[your_height][your_length] = '*'
                print(maze[height][length], end = ' ')
            print()
        while(maze[your_height][your_length] != ' '):
            move = input("")
            if move == 'w':
                your_height =your_height - 1
                if(maze[your_height][your_length] == '█'):
                    your_height= your_height+ 1
            elif move == 'a':
                your_length= your_length - 1
                if(maze[your_height][your_length] == '█'):
                    your_length=your_length+ 1
            elif move == 's':
                your_height =your_height +1
                if(maze[your_height][your_length] == '█'):
                    your_height= your_height- 1
            elif move == 'd':
                your_length= your_length + 1
                if(maze[your_height][your_length] == '█'):
                    your_length = your_length -1
            else:
                print("Please use a w-a-s-d input")
            if(maze[your_height][your_length] == '█'):
                print("Uh Oh, Your pick lock has hit a wall.")
            if(your_length == 12 and your_height == 11):
                next = input('Congratulations! You found the have successfully pick locked the chest. Press enter to continue:')
                if next == '':
                    finish = True
                    os.system('clear')
                    print()
                else:
                    finish = True
                    os.system('clear')
                    print()
def maze():
    finish = False
    your_height2= 1
    your_length2 =0
    os.system('clear')
    for char in "You need to complete this maze in order to pick lock the chest. Use the WASD keys in order to move. The dot (*) represents your pick lock. Good luck!":
        time.sleep(0.03)
        print(char, end = '', flush = True)
    time.sleep(1)
    os.system('clear')
    while(finish == False):
        os.system('clear')
        maze2 = [['█','█','█','█','█','█','█','█','█','█'],
            [' ',' ','█',' ',' ','█','█',' ','█','█'],
            ['█',' ',' ',' ','█','█',' ',' ','█','█'],
            ['█','█','█',' ',' ',' ',' ','█','█','█'],
            ['█','█','█',' ','█',' ',' ',' ','█','█'],
            ['█',' ',' ',' ','█',' ','█',' ','█','█'],
            ['█',' ','█','█','█',' ','█',' ',' ','█'],
            ['█',' ','█','█','█','█','█','█','█','█']]
        for height2 in range(0,2+your_height2):
            for length2 in range(0,2+your_length2):
                maze2[your_height2][your_length2] = '*'
                print(maze2[height2][length2], end = ' ')
            print()
        while(maze2[your_height2][your_length2] != ' '):
            move = input("")
            if move == 'w':
                your_height2 =your_height2 - 1
                if(maze2[your_height2][your_length2] == '█'):
                    your_height2= your_height2+ 1
            elif move == 'a':
                your_length2= your_length2 - 1
                if(maze2[your_height2][your_length2] == '█'):
                    your_length2=your_length2+ 1
            elif move == 's':
                your_height2 =your_height2 +1
                if(maze2[your_height2][your_length2] == '█'):
                    your_height2= your_height2- 1
            elif move == 'd':
                your_length2= your_length2 + 1
                if(maze2[your_height2][your_length2] == '█'):
                    your_length2 = your_length2 -1
            else:
                print("Please use a w-a-s-d input")
            if(maze2[your_height2][your_length2] == '█'):
                print("Uh Oh, Your pick lock has hit a wall.")
            if(your_length2 == 1 and your_height2 == 7):
                next = input('Congratulations! You found the have successfully pick locked the chest. Press enter to continue:')
                if next == '':
                    finish = True
                    os.system('clear')
                    print()
                else:
                    finish = True
                    os.system('clear')
                    print()


def dot_game():
    pick_lock_completion = 0
    dot = 0
    while pick_lock_completion < 100:
        for char in "\nWhen you see the green dot, press enter.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for dot in range(0,10):
                print(Dot_game[dot])
                try:
                    player_input = inputimeout(prompt = "", timeout = 1.00)
                    if(player_input == ""):
                        break
                except Exception:
                    continue
        if(dot < 3 or dot == 11 or dot == 2 or dot == 13):
            print("You missed your chance, you try again")
            Dot_game.insert(1, "🔴") # Inserts a red dot BEFORE index 2
            time.sleep(2)
            os.system("clear")
        elif (dot < 5 and dot >3 or dot == 9 or dot == 10):
            print("You are so close. But it was not fully unlocked.")
            Dot_game.insert(4, "🟡") # Inserts a yellow dot BEFORE index 2
            pick_lock_completion += 20
            print("Completion : ",pick_lock_completion)
            time.sleep(2)
            os.system("clear")
        elif(dot < 8 and dot > 5):
            print("Nice skills! The chest is open!")
            pick_lock_completion += 100
            time.sleep(1.5)
            os.system("clear")




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
Dot_game = ["🔴", "🔴", "🔴", "🟡", "🟡", "🟢", "🟢", "🟢", "🟢", "🟡", "🟡", "🔴", "🔴", "🔴"]
Sneak_game = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Lock_game =  [['0','1','0','0','0','0','0','0','0'],
              ['0','1','1','1','0','0','1','1','0'],
              ['0','0','0','1','1','1','1','0','0'],
              ['0','0','0','1','0','1','0','0','0']]

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
        data = str(json.load(file))
        try:
            progress = int(data[14])*11
        except:
            progress = 0
        time.sleep(2)
        # int(data['progress'])
if game == 0:
    progress = 0
if progress == 0: #Senario 1
    os.system('clear')
    for char in "You are a pirate and are part of an organization called, Creed of Wolfheim.\nThe Creed of Wolfheim are having a conflict with another organization called the The Akatsuki of the Shadows.\nYour mission is to travel to Conomi a country, and assassinate the leader of The Akatsuki of the Shadows to stop the conflict.\nYou must be off to your journey now, Mr. Edward Kensmen.":
        time.sleep(0.025)
        print(char, end="", flush=True)
    time.sleep(3)
    os.system('clear')
    for char in "Time: 10:30 AM\nKenzuma Island\nOn the port, meeting with Johan to gather a crew.":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(3)
    os.system('clear')
    for char in "Johan: Oi Captain, I got some mates that work at the Tavern.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(2)
    for char in "Type yes or no to choose a decision.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    choice1 = get_player_choice("Do you want to bring them along?(yes or no)", ["yes", "no"])
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
        time.sleep(0.8)
    if choice1 == 'no':
        for char in "I don't think we need 'em. I have others in mind.\n":
            time.sleep(0.04)
            print(char, end="", flush=True)
        time.sleep(0.5)
        for char in "Johan: You know, my bunch couldn't really fall below your standards, I ought to go get em' right about.":
            time.sleep(0.04)
            print(char, end="", flush=True)
        time.sleep(1)
    os.system('clear')
    for char in "12:00 PM\nAfter gathering the crew together, Johan introduces you to Leroy, Will, Juan, and others.\n":
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
    choice2 = get_player_choice("Do you want to sneak into the warehouse(sneak) or have a shootout(shootout)?", ["sneak","shootout"])
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
        time.sleep(0.5)
        result = sneak_game()
        if result == False:
            for char in "Enemy: Oi! What are you doing here!\n":
                time.sleep(0.05)
                print(char, end="", flush=True)
            time.sleep(0.6)
            combat_game()
        time.sleep(2)
        os.system('clear')
        i = random.randint(0,5)
        for char in JohanSneakPhrases[i]:
            time.sleep(0.07)
            print(char, end="", flush=True)
        time.sleep(0.5)
        second = sneak_game()
        if second == False:
            for char in "Enemy: Oi! What are you doing here!\n":
                time.sleep(0.05)
                print(char, end="", flush=True)
            time.sleep(0.6)
            combat_game()
        os.system('clear')
        i = random.randint(0,5)
        for char in JohanSneakPhrases[i]:
            time.sleep(0.07)
            print(char, end="", flush=True)
        time.sleep(0.5)
        third = sneak_game
        if third == False:
            for char in "Enemy: Oi! What are you doing here!\n":
                time.sleep(0.05)
                print(char, end="", flush=True)
            time.sleep(0.6)
            combat_game()
        for char in "Excellent work team! We have made it into the warehouse.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
    if choice2 == 'shootout':
        os.system('clear')
        for char in "You shoot 3 enemies and alarm the whole camp of your presence.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Enemy: Oi! Get em'!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        combat_game()
        for char in "Enemy 2: You will pay!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        combat_game()
        os.system('clear')
        for char in "After fighting for a long time, you were successful in defeating the enemies.":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
    with open('save.txt', 'w') as file:
        file.write("{\"progress\": 33}")
    with open('save.txt', 'r') as file:
        data = json.load(file)
        progress = int(data['progress'])
if progress == 33: #Senario 2
    os.system('clear')
    for char in "2:00 AM\nIn the warehouse\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Johan: Captain! Look at all this loot!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Will: 200 cannon balls, 5 cannons, 100,000 dollars worth of jewlery, and 5 ropes that are 100 meters long.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.8)
    for char in "Great work lads! Lets get this into the ship.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    os.system('clear')
    for char in "4:00 AM\nAt the port\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Leroy: Oi! Captain, what about the equipment for us lads?":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.7)
    for char in "I will go back to the warehouse to see if we missed something. Juan, come with me.":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.6)
    for char in "Juan: Yes Captain!":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    os.system('clear')
    for char in "4:00 AM\nAt the warehouse\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Search around and see if you can find some hidden treasure.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Juan: Aye Aye Captain!":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    os.system('clear')
    for char in "3:40 AM\nYou and Juan search the warehouse and other surround building.":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Juan: Captain! I found a locked chest!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Great work lad! I will lock pick it while you go find more.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    maze()
    os.system('clear')
    for char in "Juan: Oi Captain! There is anothere one here!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.7)
    for char in "Good work! Go see if there are still more.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1.5)
    dot_game()
    os.system('clear')
    for char in "Juan: Captain come look!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1.5)
    for char in "What is it mate?\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Juan: It's a secret vault in the floor!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "There is a keyhole. I could probably open this.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    big_maze()
    for char in "There we go. Its unlocked now.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Juan: Great work Captain!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.6)
    for char in "Now lets see what is inside this vault\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1.5)
    for char in "Juan: Captain! Look at all these equipment they were hidding.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.6)
    for char in "HAHAHAHA! Great work mate! This is more than enough for all of us!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.6)
    for char in "Call yer mates over to help bring all this back to the ship.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(0.5)
    for char in "Juan: Yes Captain!\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    game = {"progress": 66}
    with open('save.txt', 'w') as file:
        file.write(json.dumps(game))
if progress == 66: #Senario 3
    os.system('clear')
    for char in "*Turns head*\nWhat's this?\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "*Grabs the mysterious looking fragemnt*\nWhat in the western lake is this?\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    choice3 = get_player_choice("Do you want to keep it?(yes or no)", ["yes", "no"])
    if choice3 == 'yes':
        for char in "You put it into your pocket\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "*You hear a voice*\n๒єฬคгє ๏Ŧ Շђє ๔คภﻮєг.เՇร ς๏๓เภﻮ\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(2)
        for char in "Eh?! Who's there!\n*Turns around*\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Leory: Captain! We are here to help you!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Excellent! Lets get all this equipment onto the ship then.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "*While moving the boxes you feel a presence watching you*\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(2)
        for char in "Lets move out! We got all the boxes\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "i̷̧̡̲̼̼͇͖̥̲̭̬̬͚̠͚͓̼̜̥͗̇̀̿̇̀̈́͠ͅj̶̧̢̡̙͍̞̖̥͉͈̭̺̞͓͎̥͍̜̘̆̈́̅̀̃̀́̆͜i̸̢͕̻̣̭̞͖͎̲̘͓̙̲͔̹̰͈͚͙̖͛̐͐̐͜ͅͅș̶̨͙̣̦͎̱̱͎̞̞̾̽͐͘͜͝ę̶̧̢̠̙̩̝̪̤̱͇̭̜̦̪̙̫́͛̒͗̌͊̃͑͂͒͒̅̈́͒͗̕˚̴̢̨̫̺̀̏͐̇̅̓̔̆̑̂͂̈́̈́̔̈͒̈́̄́̾̕͝͝∑̷̼̜̱͎̬̜͋̾̽̈́̀́̚k̶͈̺̓̇̏̎̅̓̇̉́͋̍̏̀̑̾̕̕͠͠ę̸̧̨̛̱̫̖̱͕͎͐̐̄̋͋͛͆͊͗͛̓̉̋͊́͘͝r̴̜͚̰̉̊̇͆̿̈́:W乇'尺乇 Wﾑｲᄃんﾉ刀ム ﾘのひ...\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(2)
    if choice3 == 'no':
        for char in "Ehhh. Probably nothing special.\n*throws away the mysterious fragement*\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Leory: Captain! We are here to help you!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Excellent! Lets get all this equipment onto the ship then.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "*While moving the boxes of equipment you feel a presence leave*\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
    for char in "5:00 AM\nOn the ship getting ready to sail.\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    for char in "Juan: Are you ready Captain?\n":
        time.sleep(0.05)
        print(char, end="", flush=True)
    time.sleep(1)
    choice4 = get_player_choice("Are you ready?(yes or no)", ["yes", "no"])
    if choice4 == 'yes':
        for char in "Lets sail!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(2)
        os.system('clear')
        for char in "7:00 AM\n Your ship sails towards Conomi.\nYou are ready now, Edward Kensmen.":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(2)
    if choice4 == 'no':
        os.system('clear')
        for char in "One moment lads! Let me grab all my gear.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "Will: Fine Captain. How about Juan sails and you do yur things.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1.4)
        for char in "7:05 AM\nIn Captain's room.\nYou grab all your gear and feel the ship moving.\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "*You go outside*\n Let's get ready for war men!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(1)
        for char in "All: Aye! Aye! Captain!\n":
            time.sleep(0.05)
            print(char, end="", flush=True)
        time.sleep(2)
        for char in "THE END!\nTHANKS FOR PLAYING.\nRUN CODE AGAIN TO LOAD OR PLAY NEW GAME":
            time.sleep(0.5)
            print(char, end="", flush=True)
        time.sleep(3)
        quit()
