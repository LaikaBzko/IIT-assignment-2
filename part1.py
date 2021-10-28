    ##############################################################################################################
    ##############################################################################################################
    ####  Author: Laika Marshall                                                                              ####
    ####  Date Created: 27/04/2021                                                                            ####
    ####  Date Last Changed: 2/05/2021                                                                        ####
    ####  a simple program to calculate warp speed and travel times, from the film and TV franchise Star Trek ####
    ####  Input: none     Output: none                                                                        ####
    ##############################################################################################################
    ##############################################################################################################

################################################################################################################################################################
# constants and libraries
################################################################################################################################################################
from playsound import playsound
from pyfiglet import Figlet                                                     # for the big text

fig = Figlet(font='starwars')                                                   # yes I chose star wars for a star trek program
scaleSet = False
DESTINATIONS = ["Theta Eridani (Acamar III)", "Alcyone (Eta Tauri)", "Aldebaran III (Alpha Tauri)", "Algol(Alpha Aquilae)", "Alpha Centauri", "Alpha Eridani", "Altair III, IV, VI(Alpha Aquilae)", "Antares IV (Alpha Scorpii)", "Arcturus (Alpha Bootis)", "Bellatrix (Gamma Orionis)", "Beta Aurigae", "Betelguese (Alpha Orionis)", "Cait (15 Lynics)", "Caldos IV", "Canopus (Alpha Carinae), Alpha Carinae II, V", "Capella IV (Alpha Aurigae)", "Cor Caroli V (Alpha Canum Venaticorum)", "Deneb IV, II, IV, V (Alpha Cygni), Alpha Cigni IX", "Epsilon Hydrae VII", "Epsilon Indi", "the Galactic Core", "Gamma Hydrae II, IV (Neutral Zone)", "Gamma Tauri IV", "Gamma Trianguli VI", "Izar (Epsilon Bootis)", "Merak II (Beta Ursae Majoris)", "Mintaka III (Delta Orionis)", "Mira (Omicron Ceti), Omicron Seti III", "Mizar II (Zeta Ursae Majoris)", "Ocampa", "Pollux", "Regulus", "Rigel"]
DISTANCES = [49.45941, 112.7481, 19.96558, 28.45966, 1.347513, 44.09511, 5.143238, 185.1992, 11.255464, 74.52131, 25.17811, 131.0715, 52.2507, 61.32028, 95.88468, 12.93919, 33.78625, 990.17411, 41.44546, 3.626481, 7910.316, 40.50542, 47.24022, 36.05491, 64.31363, 24.35059, 280.9202, 128.3785, 23.9656, 22995.1, 10.33768, 23.76038, 236.9848]

################################################################################################################################################################
# misc functions
################################################################################################################################################################

def login():                                                                    # a reference to star trek (2009) and the late Anton Yelchin (may he rest in peace)
    print(fig.renderText('LCARS SECURE LOGIN'))
    playsound("assets/clearance.wav", block = False)
    while True:
        commandCode = input(">> PLEASE INPUT COMMAND AUTHORISATION CODE: ")
        if commandCode == "9-5-victor-victor-2":                                # this is the password
            playsound("assets/authAccepted.wav")
            print(">> AUTHORISATION CODE ENS. CHECKOV RECOGNISED")
            break
        else:
            print(">> AUTHORISATION NOT RECOGNISED. PLEASE TRY AGAIN")
            playsound("assets/authDenied.wav", block = False)


def menu():                                                                     # the main menu
    print(fig.renderText('LCARS ACCESS 642'))
    playsound("assets/beep12.wav")
    print(">> LCARS NAGIVATION INTERFACE")
    print(">> PLEASE SELECT AN OPTION")
    print(">> 1. NAVIGATION DATABASE ")
    print(">> 2. COURSE CALCULATION")
    print(">> 3. LOGOUT LCARS NAVIGATION SYSTEM")
    userChoice = int(input(">>> "))
    if userChoice == 1:                                                         # goes to option 2
        playsound("assets/accessingDB.wav")
        destinationsMenu()
    elif userChoice == 2:
        playsound("assets/beep3.wav", block = False)                            # goes to option 1
        navigation()
    elif userChoice == 3:                                                       # quit (doesnt have its own function, why would it?)
        while True:
            playsound("assets/deactivateA.wav")
            logoutConf = input(">> CONFIRM LCARS LOGOUT (Y/N)")
            if logoutConf == "y":
                playsound("assets/deactivateB.wav")
                exit()

            elif logoutConf == "n":
                playsound("assets/Cancelled.wav")
                menu()
            else:
                print(">> INVALID RESPONSE")
                playsound("assets/restate.wav")
                input("...")
                menu()


def introduction():
    print(">> WELCOME ENSIGN CHECKOV (PAVEL ANDREOVICH), TO THE STARFLEET ASSISTANT TO NAVIGATION TEXT-BASED APPLICATION (OR S.A.N.T.A)")
    print(">> THIS TOOL WILL ASSIST IN THE CALCULATION OF WARP FACTORS TO OTHER UNITS OF SPEED, AS WELL AS ACCESS ASTROMETRIC DATABASES TO HELP CALCULATE THE TRAVEL TIME TO PLANETARY BODIES")
    print(">> THE WARP SELECTION, BETWEEN TOS AND TNG WARP SCALES HELPS FACTOR FOR DEALING WITH POTENTIAL TIME TRAVEL SCENARIOS, UN-UPGRADED 23RD CENTURY SHIPS, OR ANY OTHER REASON TO NEED THE OLD WARP SCALE")
    print(">> IN A SITUATION WHERE A PROMPT CONTAINING ONLY THREE DOTS, SUCH AS THE FOLLOWING PROMPT, PRESS THE ENTER KEY ON YOUR KEYBOARD TO PROGRESS THE PROGRAM")
    input("...")
    playsound("assets/beep9.wav", block = False)

################################################################################################################################################################
# menu option 1 - navigation database
################################################################################################################################################################

def destinationsMenu():                                                         # menu choice 1, shows informations on planets
    print(fig.renderText('LCARS ACCESS 912'))
    print(">> LCARS NAVIGATION DATABASE")
    print(">> PLEASE SELECT AN OPTION")
    print(">> 1. LIST ALL PLANETS")
    print(">> 2. SELECT ENTRY")
    print(">> 3. RETURN TO MENU")
    destinationMenuChoice = int(input(">>> "))
    if destinationMenuChoice == 1:
        showAllDestinations()
        playsound("assets/beep5.wav", block = False)
    elif destinationMenuChoice == 2:
        showSpecificDestionation()
        playsound("assets/beep6.wav", block = False)
    elif destinationMenuChoice == 3:
        menu()
    else:
        print(">> INVALID RESPONSE")
        playsound("assets/restate.wav")
        input("...")
        destinationsMenu()


def showAllDestinations():                                                      # iterates through planet lists and returns to destinations menu
    playsound("assets/beep10.wav", block = False)
    for i in range(len(DESTINATIONS)):
        if i < 9:                                                               # keeps the output consistent, provides padding for single didget numbers
            print("PLANETARY ENTRY", i+1, "  | ", DESTINATIONS[i], "CURRENTLY", DISTANCES[i], "PARSECS AWAY")
        else:
            print("PLANETARY ENTRY", i+1, " | ", DESTINATIONS[i], "CURRENTLY", DISTANCES[i], "PARSECS AWAY")
    input("...")
    playsound("assets/beep1.wav", block = False)
    destinationsMenu()


def showSpecificDestionation():
    playsound("assets/beep13.wav", block = False)                                                 #selects and outputs a planet and its information and returns to destinations menu
    print(">> PLEASE SELECT A DATABASE ENTRY")
    planetChoice = int(input(">>> "))
    if planetChoice < 33:
        print(">> ENTRY", planetChoice)
        playsound("assets/accessFile.wav")
        print(">> PLANET", DESTINATIONS[planetChoice-1])
        print(">>", DISTANCES[planetChoice-1], "PARSECS FROM SECTOR 001")
        playsound("assets/beep2.wav", block = False)
        input("...")
        destinationsMenu()
    elif planetChoice == 42:                                                    # a hitch-hikers guide to the galaxy reference :-)
        print(">> ENTRY 42")
        playsound("assets/prioClearance.wav")
        print(">> THE DINER AT THE END OF THE UNIVERSE")
        print(">> TOO FAR TO GET TO, ALTERNATE IMPROBABLE TRANSPORT METHOD NEEDED")
        print(">> SO LONG, AND THANKS FOR ALL THE FISH!")
        input("...")
        destinationsMenu()
    else:
        print(">> INVALID RESPONSE")
        playsound("assets/restateQ.wav")
        input("...")
        showSpecificDestionation()

################################################################################################################################################################
# menu option 2 - course calculation subsystem
################################################################################################################################################################

def navigation():                                                               # calculations menu, menu choice 2
    print(fig.renderText('LCARS ACCESS 11-1989'))
    playsound("assets/beep12.wav")
    print(">> LCARS COURSE CALCULATION SUBSYSTEM")
    print(">> PLEASE SELECT AN OPTION")
    print(">> 1. CALCULATE WARP FACTOR EQUIVILENTS")
    print(">> 2. CALCULATE DESTINATION INFORMATION")
    print(">> 3. RETURN TO MENU")
    navigationChoice = int(input(">>> "))
    if navigationChoice == 1:
        warpCalculations()
        playsound("assets/beep7.wav")
    elif navigationChoice == 2:
        destinationCalculations()
        playsound("assets/beep8.wav")
    elif navigationChoice == 3:
        menu()
    else:
        print(">> INVALID RESPONSE")
        playsound("assets/restate.wav")
        input("...")
        menu()


def warpCalculations():                                                         # navigation choice 1
    playsound("assets/awaitingInput.wav", block = False)
    warpInput = float(input(">> PLEASE SELECT A WARP FACTOR: "))

    if warpInput >= 10 and scaleType == 1:
        print(">> ERROR! WARP FACTOR SELECTED IS ABOVE WARP 10 THRESHOLD")
        print(">> PLEASE SELECT A VALID WARP FACTOR")
        input("...")
        playsound("assets/errorbeep.wav")
        warpCalculations()

    warpC = calcWarpToC(warpInput)
    warpKMS = calcWarpCToKMS(warpC)
    warpAUH = calcWarpToAUH(warpC)
    warpPCH = calcWarpToPCH(warpAUH)
    warpLYH = calcWarpToLYH(warpPCH)
    playsound("assets/beep10.wav", block = False)
    print(">> ")
    print(">> WARP", warpInput, "IS", warpC, "TIMES THE SPEED OF LIGHT")
    print(">> WARP", warpInput, "IS", warpKMS, "KILOMETERS PER SECOND")
    print(">> WARP", warpInput, "IS", warpAUH, "ASTRONOMICAL UNITS PER HOUR")
    print(">> WARP", warpInput, "IS", warpPCH, "PARSECS PER HOUR")
    print(">> WARP", warpInput, "IS", warpLYH, "LIGHTYEARS PER HOUR")
    input("...")
    navigation()


def destinationCalculations():                                                  # navigation choice 2
    print(">> PLEASE SELECT A DESTINATION FROM PLANETARY DATABASE")
    playsound("assets/accessingDB.wav")
    destinationChoice = int(input(">>> "))
    if destinationChoice > 33:
        print(">> PLEASE SELECT A NUMERICAL VALUE BETWEEN 1 AND 33")
        playsound("assets/definepls.wav")
        input("...")
        destinationCalculations()

    destinationPlanet = DESTINATIONS[destinationChoice-1]
    destinationDistance = DISTANCES[destinationChoice-1]

    print(">> PLANET", destinationPlanet, "SELECTED")
    playsound("assets/awaitingInput.wav")
    destinationWarpInput = float(input(">> PLEASE SELECT A WARP FACTOR: "))

    if destinationWarpInput >= 10 and scaleType == 1:
        print(">> ERROR! WARP FACTOR SELECTED IS ABOVE WARP 10 THRESHOLD")
        print(">> PLEASE SELECT A VALID WARP FACTOR")
        playsound("assets/errorbeep.wav")
        input("...")
        destinationCalculations()

    warpC = calcWarpToC(destinationWarpInput)
    warpKMS = calcWarpCToKMS(warpC)
    warpAUH = calcWarpToAUH(warpC)
    warpPCH = calcWarpToPCH(warpAUH)
    warpLYH = calcWarpToLYH(warpPCH)
    hoursToDestination = destinationDistance/warpPCH
    if hoursToDestination > 36:
        print(">>", destinationPlanet, "IS", (convertToDays(hoursToDestination)[0]), "DAYS AND",  (convertToDays(hoursToDestination)[1]), "HOURS AWAY AT:") # if a journey is more than 36 hours, it automatically converts to days + hours
    else:
        print(">>", destinationPlanet, "IS", hoursToDestination, "HOURS AWAY AT:")  # standard response
    print(">> WARP", destinationWarpInput)                                      # prints calculations of alternate speed metrics
    print(">>", warpKMS, "KILOMETERS PER SECOND")
    print(">>", warpAUH, "ASTRONOMICAL UNITS PER HOUR")
    print(">>", warpPCH, "PARSECS PER HOUR")
    print(">>", warpLYH, "LIGHTYEARS PER HOUR")
    print(">> WITH A TOTAL DISTANCE OF", destinationDistance, "PARSECS")
    playsound("assets/beep9.wav", block = False)
    input("...")
    navigation()


def calcWarpToC(warpFactor):                                                    # calculates a warp factor to c, pc, km/s
    if scaleType == 0:
        warpC = warpFactor ** 3                                                 # old warp factor is just Factor^3*c
    if scaleType == 1:
        warpC = warpFactor ** (10/3)                                            # new warp factor is Factor^10/3*c
    return warpC


def calcWarpCToKMS(warpC):                                                      # calculates warp speed to KM/S
    warpKMS = warpC*299792.458
    return warpKMS


def calcWarpToAUH(warpC):                                                       # calculates warp speed to AU/H
    warpAUH = warpC*7.21436
    return warpAUH


def calcWarpToPCH(warpAUH):                                                     # calculates warp speed to PC/H
    warpPCH = warpAUH*0.000004848137
    return warpPCH


def calcWarpToLYH(warpPCH):                                                     # calculates warp speed to LY/H
    warpLY = warpPCH*3.261564
    return warpLY


def convertToDays(time):                                                        # converts hours to days + hours, called when travel time > 36 hours
    days = 0
    while True:
        if time > 24:
            time = time - 24
            days = days + 1
        else:
            daysAndHours = [days,time]
            return daysAndHours
            break

################################################################################################################################################################
# the actual main() program
################################################################################################################################################################

def main():
    login()                                                                     # the code is "9-5-victor-victor-2"
    introduction()
    while True:
        print(">> SELECT WARP SCALE")                                           # runs at start, selects old/new warp scale
        scaleChoice = int(input(">> ORIGINAL (1) OR THE NEXT GENERATION (2): "))
        if scaleChoice == 1:
            global scaleType
            scaleType = 0
            playsound("assets/tos-intercom.wav")
            break
        elif scaleChoice == 2:
            scaleType = 1
            playsound("assets/beep3.wav")
            break
        else:
            print(">> PLEASE INPUT A VALID SELECTION")
            return
    playsound("assets/ready.wav")
    menu()

################################################################################################################################################################
# and then we call main
################################################################################################################################################################

main()

################################################################################################################################################################
# this was a triumph! I'm making a note here, huge success. It's hard to overstate my satisfaction
################################################################################################################################################################
