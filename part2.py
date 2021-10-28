    ##############################################################################################################
    ##############################################################################################################
    ####  Author: Laika Marshall                                                                              ####
    ####  Date Created: 01/05/2021                                                                            ####
    ####  Date Last Changed: 02/05/2021                                                                       ####
    ####  a simple program to calculate warp speed and travel times, from the film and TV franchise Star Trek ####
    ####  Input: none     Output: none                                                                        ####
    ##############################################################################################################
    ##############################################################################################################

################################################################################################################################################################
# globals, constants and libraries
################################################################################################################################################################
import random
from tkinter import *
from playsound import playsound

root = Tk()                                                                     # alias the main window
root.geometry("850x450")                                                        # set the sizes
planetSelection = "none"                                                        # to help avoid errors

DESTINATIONS = ["Theta Eridani (Acamar III)", "Alcyone (Eta Tauri)", "Aldebaran III (Alpha Tauri)", "Algol(Alpha Aquilae)", "Alpha Centauri", "Alpha Eridani", "Altair III, IV, VI(Alpha Aquilae)", "Antares IV (Alpha Scorpii)", "Arcturus (Alpha Bootis)", "Bellatrix (Gamma Orionis)", "Beta Aurigae", "Betelguese (Alpha Orionis)", "Cait (15 Lynics)", "Caldos IV", "Canopus (Alpha Carinae), Alpha Carinae II, V", "Capella IV (Alpha Aurigae)", "Cor Caroli V (Alpha Canum Venaticorum)", "Deneb IV, II, IV, V (Alpha Cygni), Alpha Cigni IX", "Epsilon Hydrae VII", "Epsilon Indi", "the Galactic Core", "Gamma Hydrae II, IV (Neutral Zone)", "Gamma Tauri IV", "Gamma Trianguli VI", "Izar (Epsilon Bootis)", "Merak II (Beta Ursae Majoris)", "Mintaka III (Delta Orionis)", "Mira (Omicron Ceti), Omicron Seti III", "Mizar II (Zeta Ursae Majoris)", "Ocampa", "Pollux", "Regulus", "Rigel"]
DISTANCES = [49.45941, 112.7481, 19.96558, 28.45966, 1.347513, 44.09511, 5.143238, 185.1992, 11.255464, 74.52131, 25.17811, 131.0715, 52.2507, 61.32028, 95.88468, 12.93919, 33.78625, 990.17411, 41.44546, 3.626481, 7910.316, 40.50542, 47.24022, 36.05491, 64.31363, 24.35059, 280.9202, 128.3785, 23.9656, 22995.1, 10.33768, 23.76038, 236.9848]

################################################################################################################################################################
# functions
################################################################################################################################################################

def introduction():                                                             # triggered when the menu option 'introduction' is clicked
    window = Toplevel()                                                         # creates a new window
    window.geometry('850x200')
    introductionLabel = Label(window, text ="Welcome to S.U.G.M.A: STARFLEET User-driven Graphical speed-Measurment Application.\nThis tool is designed to calculate warp factors to real-space speeds,\n as well as calculating the distances to planets that are members of the United Federation of Planets and the estimated travel time.\n There are three ways to use this tool: \n 1. Select a planet from the side bar to view the distance from sector-001 (earth).\n 2. Input a warp factor, and press the 'calculate warp speed' button to see real-space equivilents. \n 3. by selecting a planet and inputting a warp factor, you can calculate the previously mentioned data as well as travel time. \n This program also supports the outdated original warp scale, which can be changed with the selector in the top right corner.\n To use the file import functionality, select the 'load' option in the menu bar. \n Similarly, to use the save function, select the 'save' option in the menu bar. \n The 'exit' option is also located in the menu bar.")
    introductionLabel.pack()

def retrieveWarp():                                                             # handles warp scale swaps
    if warpScaleType.get() == 1:
        newScale = False
    elif warpScaleType.get() == 2:
        newScale = True
    return newScale


def retrieveDest(e):                                                            # this procs whenever the list element has a new selection
    chance = (random.randint(1, 10))                                            # 1 in 10 chance to proc a computer sfx
    if chance == 5:
        playsound("assets/accessingDB.wav", block = False)
    planetSelectionTemp = destinationBox.curselection()
    global planetSelection                                                      # this'll be needed elsewhere
    planetSelection = planetSelectionTemp[0]
    destinationInfo.configure(text = DESTINATIONS[planetSelection])             # because for some reason tkinter passes it back as a single element tuple?
    distanceText = DISTANCES[planetSelection], "Parsecs"
    distanceInfo.configure(text = distanceText)
    return planetSelection


def save():                                                                     # because I couldn't leave load() alone
    global planetSelection
    outputFile = open('output.txt', "w")
    warpTemp = (warpFactorEntry.get())
    planetOutput = str(planetSelection)
    warpOutput = str(warpTemp)
    outputContents = ["planet number:\n", planetOutput, "\nwarp factor:\n", warpOutput]
    outputFile.writelines(outputContents)
    playsound("assets/transferComp.wav", block = False)


def load():                                                                     # to satisfy part 3
    playsound("assets/accessing.wav")
    global planetSelection
    Input = open('input.txt')
    contents = Input.readlines()
    planetSelection = int((contents[1]))
    warpFactor = (contents[3])
    destinationBox.select_set(planetSelection)
    warpFactorEntry.insert(0,warpFactor)
    destinationInfo.configure(text = DESTINATIONS[planetSelection])             # because for some reason tkinter passes it back as a single element tuple?
    distanceText = DISTANCES[planetSelection], "Parsecs"
    distanceInfo.configure(text = distanceText)


def calcWarpSpeed():                                                            # takes input from the text field and calls other calculation functions
    warpFactorTemp = (warpFactorEntry.get())
    if warpFactorTemp == '':                                                    # a cool take on error handling
        playsound("assets/provideData.wav", block = False)
        return
    warpFactor = float(warpFactorTemp)
    if warpFactor >= 10 and retrieveWarp() == True:                             # warp 10 is impossible with the new scale
        playsound("assets/errorbeep.wav", block = False)
        calcLightSpeedEntry.configure(text = "error!")
        calcLightYearsEntry.configure(text = "Warp 10")
        calcKMSEntry.configure(text = "threshold")
        calcAUEntry.configure(text = "has been")
        calcPCEntry.configure(text = "exceeded!")
        return                                                                  # if warp 10 is input with the new warp scale selected, throws an error and ends the function

    playsound("assets/beep1.wav", block = False)                                # if all the validation passes, this calls functions and sets the output boxes
    global warpPCH
    warpC = calcWarpToC(warpFactor)
    warpKMS = calcWarpCToKMS(warpC)
    warpAUH = calcWarpToAUH(warpC)
    warpPCH = calcWarpToPCH(warpAUH)
    warpLYH = calcWarpToLYH(warpPCH)
    calcLightSpeedEntry.configure(text = warpC)
    calcLightYearsEntry.configure(text = warpLYH)
    calcKMSEntry.configure(text = warpKMS)
    calcAUEntry.configure(text = warpAUH)
    calcPCEntry.configure(text = warpPCH)
    return warpPCH


def calcTravel():
    global planetSelection
    if planetSelection == "none":                                               # handling a lack of selection
        playsound("assets/specifyPerams.wav", block = False)
        return

    playsound("assets/beep2.wav", block = False)                                # at this point validation has passed
    destinationPlanet = DESTINATIONS[planetSelection]
    dPlanetDistance = DISTANCES[planetSelection]                                # set our 'database'
    warpPCH = (calcWarpSpeed())                                                              # we need this for the next line
    hoursToDestination = dPlanetDistance/warpPCH
    if hoursToDestination < 36:                                                 # handling days/hours calculations
        timeInHours = (0, "Days,", hoursToDestination, "Hours")
        toDestination.configure(text = timeInHours)
    elif hoursToDestination > 36:
        days = (convertToDays(hoursToDestination)[0])
        hours = (convertToDays(hoursToDestination)[1])
        timeInDaysAndHours = (days, "Days,", hours, "Hours")
        toDestination.configure(text = timeInDaysAndHours)
    return


def Engage():
    playsound("assets/engage.mp3", block = False)


def calcWarpToC(warpFactor_input):                                              # calculates a warp factor to c, pc, km/s
    scale=(retrieveWarp())
    if scale == False:
        warpC = warpFactor_input ** 3                                           # old warp factor is just Factor^3*c
    if scale == True:
        warpC = warpFactor_input ** (10/3)                                      # new warp factor is Factor^10/3*c
    return warpC


def calcWarpCToKMS(warpC_input):                                                # calculates warp speed to KM/S
    warpKMS = warpC_input*299792.458
    return warpKMS


def calcWarpToAUH(warpC_input):                                                 # calculates warp speed to AU/H
    warpAUH = warpC_input*7.21436
    return warpAUH


def calcWarpToPCH(warpAUH_input):                                               # calculates warp speed to PC/H
    warpPCH = warpAUH_input*0.000004848137
    return warpPCH


def calcWarpToLYH(warpPCH_input):                                               # calculates warp speed to LY/H
    warpLY = warpPCH_input*3.261564
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
def exit():                                                                     # its all about the immersion
    playsound("assets/deactivate.wav")
    root.destroy()
    return

################################################################################################################################################################
# GUI elements
################################################################################################################################################################

#####################
# frames
#####################
topFrame = Frame(root)                                                          # alias your frames
midFrame = Frame(root)
listFrame = Frame(root)
botFrame = Frame(root)

topFrame.grid_rowconfigure(0, weight=1)                                         # make things work how you want em to
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_columnconfigure(3, weight=1)

topFrame.grid(row=0, column=0, padx = 10, pady = 10)                            # init your frames
midFrame.grid(row=2, column=1, padx = 10, pady = 10)
listFrame.grid(row=2, column=0, padx = 10, pady = 10)
botFrame.grid(row=3, column=1, padx = 10, pady = 10)

#####################
# menu bar
#####################

mainmenu = Menu(root)
mainmenu.add_command(label = "Introduction", command = introduction)
mainmenu.add_command(label = "Save", command= save)
mainmenu.add_command(label = "Load", command= load)
mainmenu.add_command(label = "Exit", command = exit)
root.config(menu = mainmenu)

#####################
# scale select
#####################

warpScaleType = IntVar()        # for warp factor selection
RBttn = Radiobutton(topFrame, text = "TOS scale", variable = warpScaleType, value = 1, command = retrieveWarp)     # tng / tos selection
RBttn.grid(row = 0, column = 1, pady = 2, sticky="")                                                               # 1 = TOS, 2 = TNG

RBttn2 = Radiobutton(topFrame, text = "TNG scale", variable = warpScaleType, value = 2, command = retrieveWarp)
RBttn2.grid(row = 0, column = 2, pady = 2, sticky="")

warpScaleType.set(2)

#####################
# destination choice
#####################

destinationBox = Listbox(listFrame, height = 16, width = 32, bd = 3, exportselection = False)
for item in DESTINATIONS:
    destinationBox.insert(END, item)

destinationBox.grid(row = 0, column = 0)
destinationBox.bind('<<ListboxSelect>>', retrieveDest)                          # this automatically updates the selection on a click event, calls back to retrieveDest()

destScroller = Scrollbar(listFrame, orient = VERTICAL)
destinationBox.configure(yscrollcommand=destScroller.set)
destScroller.grid(row=0, column=1, sticky=NS)


#####################
# planet info
#####################

destinationInfo = Label(midFrame, text="destination", relief=SUNKEN, width = 42)    # from here on out, it's just buttons - pretty self explitory
destinationInfo.grid(row=0, column=0, padx = 5, pady=(2,10))

distanceInfo = Label(midFrame, text="distance", relief=SUNKEN, width = 24)
distanceInfo.grid(row=0, column=1, padx = 5, pady=(2,10))

timeToDestinationLabel = Label(midFrame, text = "travel time:")
timeToDestinationLabel.grid(row = 7, column = 0, padx = 5, pady = 10)

toDestination = Label(midFrame, text = "-- Hours and -- Minutes", relief = SUNKEN, width = 34)
toDestination.grid(row = 7, column = 1, padx = 2, pady = 5)

#####################
# inputs and outputs
#####################
warpFactorLabel = Label(midFrame, text="Warp Factor")
warpFactorEntry = Entry(midFrame, width = 12)

calcLightSpeedLabel = Label(midFrame, text="x Speed of Light")
calcLightSpeedEntry = Label(midFrame, width = 24, relief = "groove")

calcLightYearsLabel = Label(midFrame, text="Light years per hour")
calcLightYearsEntry = Label(midFrame, width = 24, relief = "groove")

calcKMSLabel = Label(midFrame, text="Kilometers per second")
calcKMSEntry = Label(midFrame, width = 24, relief = "groove")

calcAULabel = Label(midFrame, text="Astronomical Units per hour")
calcAUEntry = Label(midFrame, width = 24, relief = "groove")

calcPCLabel = Label(midFrame, text="Parsecs per hour")
calcPCEntry = Label(midFrame, width= 24, relief = "groove")

warpFactorLabel.grid(row = 1, column = 0, padx = 5, pady=(15,3))
warpFactorEntry.grid(row = 2, column = 0, padx = 5, pady=(2,10))
calcLightSpeedLabel.grid(row = 1, column = 1, pady=(15,3))
calcLightSpeedEntry.grid(row = 2, column = 1, pady=(2,10))
calcLightYearsLabel.grid(row = 3, column = 0, pady=(15,3))
calcLightYearsEntry.grid(row = 4, column = 0, pady=(2,10))
calcKMSLabel.grid(row = 3, column = 1, pady=(15,3))
calcKMSEntry.grid(row = 4, column = 1, pady=(2,10))
calcAULabel.grid(row = 5, column = 0, padx = 5, pady=(15,3))
calcAUEntry.grid(row = 6, column = 0, padx = 5, pady=(2,10))
calcPCLabel.grid(row=5, column = 1, padx = 5, pady=(15,3))
calcPCEntry.grid(row=6, column = 1, padx = 5, pady=(2,10))

# calculate button
calcDestButton = Button(botFrame, text = "Calculate Heading", command = calcTravel, fg = "red", bg = "light blue", relief = "groove", bd = 2, padx = 15)
calcDestButton.grid(row = 1, column = 1, padx = 5)

calcWarpButton = Button(botFrame, text = "calculate Warp speed", command = calcWarpSpeed, fg = "red", bg = "light blue", relief = "groove", bd = 2, padx = 15)
calcWarpButton.grid(row = 1, column = 0, padx = 5)

engageButton = Button(botFrame, text = "Engage!", command = Engage, fg = "red", bg = "light blue", relief = "groove", bd = 2, padx = 15)
engageButton.grid(row = 1, column = 2, padx = 5)

################################################################################################################################################################
# program init
################################################################################################################################################################
playsound("assets/ready.wav", block = False)                                    # plays on login
root.mainloop()
