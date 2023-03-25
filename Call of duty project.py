weapon = {
    "vaznev" : "Bruen Pendulum, Commando Foregrip, Otrezat Stock, True-Tac Grip",
    "tac56" : "17.5 Tundra Pro Barrel, FSS Sharkfin 90, 5.56 High Velocity, Demo Cleanshot Grip, TV Xline Pro",
    "spx" : ".300 High Velocity, Schlager Match Grip, FSS ST87 Bolt, PVZ-890 TAC Stock",
    "vel" : "Agent grip, 30 round mag, Schlager soldier grip, assault-60 stock",
    "kastov 762" : "TZL-90 V3, IG-K30 406mm, True TAC Grip, FTAC Ripper 56"
    }

perks = {
    "smg" : "double time, bomb squad or battle hardened, fast hands", 
    "ar" : "double time, bomb squad or battle hardened, focus"
    }

def getClass():
    gun = input("What is your gun? ")
    # type = input("what gun type is that? ")

    return gun + " class setup: " + weapon[gun]

def getPerks():
    type = input("Is the gun your using an 'ar' or an 'smg'? ")

    if type == "smg":
        return "perks: " + perks["smg"] 
    elif type == "ar":
        return "perks: " + perks["ar"]
    else:
        return "Please select either ar or smg"
    
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
    # if type == "smg":
    #     return gun + " class setup: " + weapon[gun] + "\nperks: " + perks["smg"] + "\nfield upgrade: " + field_upgrade["smg"]
    # elif type == "ar":
    #     return gun + " class setup: " + weapon[gun] + "\nperks: " + perks["ar"] + "\nfield upgrade: " + field_upgrade["ar"]
    # else:
    #     return "Please select either ar or smg"

def menu():
    print("Welcome to Jeeivan's ranked play guide")
    print("Abbreviations used: ar-Assault rifle, smg-Submachine gun")
    print("1. Give loadout for gun \nLoadouts available for: vaznev, tac56, spx, vel, kastov 762")
    print("2. Give perks for class")
    print("3. Give description of how to play role")
    print("4. How to use field upgrades effectively")
    print("5. Ranked play modes")
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
    else:
        print("That is not an option! Please select a number from the menu above :)")
    menu()

menu()