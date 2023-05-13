import json

weapon = {}

weapons = ("vaznev", "tac56", "vel", "kastov")

smgAttachments = {
    "muzzle" : "Bruen Pendulum, Lockshot KT85",
    "underbarrel" : "Commando Foregrip, FFS Sharkfin 90",
    "stock" : "Otrezat Stock, Markeev R7 Stock",
    "rear grip" : "True-Tac Grip, Phantom Grip"
    }

arAttachments = {
    "barrel" : "17.5 Tundra Pro Barrel, TZL-90 V",
    "underbarrel" : "Commando Foregrip, FFS Sharkfin 90",
    "stock" : "TV Xline Pro, FTAC Ripper 56",
    "rear grip" : "True-Tac Grip, Demo Cleanshot Grip"
    }

perks = {
    "smg" : "double time, bomb squad or battle hardened, fast hands", 
    "ar" : "double time, bomb squad or battle hardened, focus"
    }

def getClass():
    print("Weapons to choose from:")
    for x in weapons:
        print(x)
    gun = input("What is your gun? Or if you would like all loadouts please enter 'all' ")
    if gun == "vaznev" or gun == "tac56" or gun == "vel" or gun == "kastov":
        return gun + " class setup: " + weapon[gun]
    elif gun == "all":
        for key,value in weapon.items():
            print(key,':',value)
    else:
        return "You have not selected a weapon from the list or selected 'all'"

def getPerks():
    type = input("Is the gun your using an 'ar' or an 'smg'? ")

    if type == "smg":
        return "perks: " + perks["smg"] 
    elif type == "ar":
        return "perks: " + perks["ar"]
    else:
        return "Please select either 'ar' or 'smg'"
    
def getRole():
    role = input("Do you play 'ar', 'smg' or as a 'flex'? ")

    if role == "ar":
        return "Assualt rifles are often seen as a jack-of-all-trades weapon, featuring an overall balance of range, rate of fire, accuracy, and capacity. It is important when using an assault rifle you are holding down lanes of the map and use power positions to your advantage."
    elif role == "smg":
        return "SMG's have a very fast strafe speed when aiming down the sights, at least moderate rates of fire, and good hip-fire accuracy, making the SMG's ideal for close to medium range combat playstyles. It is important that you are playing the objective in modes like hardpoint and control, where you will be at an advantage in close quater gunfights."
    elif role == "flex":
        return "As a flex player you will need to switch between assualt and submachine depedning on the situation in the game or the map itself. For example where some maps may favour more mid-longer range gunfights it may be more favourable to use an assault rifle whereas a map that involves more close quater gunfights you will be better suited with using a submachine gun"
    else:
        return "Please select either 'ar', 'smg' or 'flex'"

def getFieldupgrade():
    fieldUpgrade = input("Pick your field upgrade. 'trophy' or 'dead silence' ")

    if fieldUpgrade == "trophy":
        return "Trophy systems are extremely effective in destroying tacticals/lethals. It is important that if you are going to be playing around the objective in game modes like hardpoint and control that you have someone running trophy systems to avoid any team mates in the objective zone getting bombarded with lethals and tacticals."
    elif fieldUpgrade == "dead silence":
        return "Dead silence is an effective tool in getting behind enemy lines and avoid you getting heard by enemy players. It is espcially effective in a game mode like search and destroy that is generally a slower game mode and where players are relying on sound cues for footsteps. Note that dead silence once activated only lasts for 10 seconds although a key point to note is killing an enemy while dead silence is active resets your dead silence allowing you to use it for an extended period."
    else:
        return "Please select either 'trophy', or 'dead silence'"

def getModes():
    mode = input("There are 3 modes in ranked play: Hardpoint-'HP', Search and Destory-'S&D' and 'Control' \nPick what mode you would like to know more about ")

    if mode == "HP":
        return "Hardpoints are locations that rotate around the map every 60 seconds. One point will be earned per second is scored when a Hardpoint is secured. If an enemy player enters the Hardpoint, the area will be contested and no points will be earned. The first team to reach 250 points wins."
    elif mode == "S&D":
        return "Only one bomb will be available in this mode. If the player holding the bomb is killed, the other players must grab the bomb and continue the mission. It takes 5 seconds to plant the bomb and 7.5 seconds to defuse it. Once the bomb is planted, the round timer will switch to a 45 second timer. If the bomb is defused, the defending team will earn a point. Respawning is not allowed in this mode, which means a round can be won if an entire team is eliminated. It is first team to win 6 rounds wins the game."
    elif mode == "Control":
        return "Like Search, Control is a round-based mode where the first one to win three separate rounds wins the whole match. Teams take turns on defense and offense. Regardless of the side, both teams begin the round with 30 shared lives. If either team runs out of lives, the match ends. But the goal is to capture two points on the map. There are three checkpoints on the circle. Completing the circle will capture the point for the offensive side. If the offense can’t capture both points in time, or they run out of lives, then the defense takes the victory. This mode is all about fast kills and learning how to spawn trap, so it will take time to learn the routes, but it’s certainly possible."
    else:
        return "Error! Please pick a mode from 'HP', 'S&D' and 'Control'"

def makeLoadout():
    print("Weapons to choose from:")
    for x in weapons:
        print(x)
    chooseGun = input("Which gun would you like to make a loadout for? ")
    if chooseGun == "vaznev":
        print(smgAttachments)
    elif chooseGun == "tac56":
        print(arAttachments)
    elif chooseGun == "vel":
        print(smgAttachments)
    elif chooseGun == "kastov":
        print(arAttachments)
    else:
        return "This is not an option! Please select from a weapon above."
    chooseMuzzle = input("Which muzzle/barrel would you like? ")
    chooseUnderBarrel = input("Which underbarrel would you like? ")
    chooseStock = input("Which stock would you like? ")
    chooseRearGrip = input("Which rear grip would you like? ")
    userAttachments = chooseMuzzle + ", " + chooseUnderBarrel + ", " + chooseStock + ", " + chooseRearGrip
    weapon[chooseGun + " personal loadout"] = userAttachments
    with open("weapons.txt", "w") as outfile:
        json.dump(weapon, outfile)
    for key,value in weapon.items():
        print(key,':',value)


def menu():
    global weapon
    with open("weapons.txt", "r") as infile:
        weapon = json.load(infile)
    print("Welcome to Jeeivan's ranked play guide")
    print("Abbreviations used: ar-Assault rifle, smg-Submachine gun")
    print("1. Give loadout for gun")
    print("2. Give perks for class")
    print("3. Give description of how to play role")
    print("4. How to use field upgrades effectively")
    print("5. Ranked play modes")
    print("6. Make your own loadout")
    usersInput = input('Enter your option here: ')
    if usersInput == "1":
        print(getClass())
    elif usersInput == "2":
        print(getPerks())
    elif usersInput == "3":
        print(getRole())
    elif usersInput == "4":
        print(getFieldupgrade())
    elif usersInput == "5":
        print(getModes())
    elif usersInput == "6":
        print(makeLoadout())
    else:
        print("That is not an option! Please select a number from the menu above :)")
    menu()

menu()

# Allow user to create own classes (look up adding to dictionary)
# for loop for weapons
# a way to show all weapon loadouts
# create your own perk
# handling complex user inputs 
# have user creat own weapon loadout
# create list of attachements for each gun
# take user input one by one for each attachment
# combine attachments and add new entry to dictionary (add all attachments to one string)
# make sure that the key is a different value - string manipulation


# look up reading and writing to file
# look up setting dictionary from text file
# reading is getting the data from the file
# writing is saving the data to the file