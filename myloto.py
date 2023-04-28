# Dont forget to change images for each person cuz stupid OCR
# Change all PlaceBets to coorect coordinatee ( Place Bets initiates the first bet after a while loop)
import pyautogui
import random
import webbrowser
import time
from datetime import datetime
import math



# Insert cash here
AmountOfMoney = 0.1

# Total lives?
Total = 10
SafetyRate = 1/4



Games = int(math.log2(AmountOfMoney/0.1)-1)

GamesTillEnd =int(1/((19/37)**Total))/(1/SafetyRate)
# List of random websites to choose from
websites = ['https://loteries.espacejeux.com/en/home']

# Open a random website from the list
# webbrowser.open(random.choice(websites))

# Wait for the website to load


# REMEMBER
# pyautogui.sleep(15)




# Get the screen size
screen_width, screen_height = pyautogui.size()

# Generate a random x and y coordinate within the screen size
x_coord = random.randint(0, screen_width)
y_coord = random.randint(0, screen_height)

# Move the mouse to the random coordinate and click it
#pyautogui.moveTo(1285, 175, duration=0.1)
#pyautogui.click()

#pyautogui.moveTo(800, 290, duration=0.1)
#pyautogui.click()

#pyautogui.typewrite('edenkozlov@gmail.com', interval=0.05)

#pyautogui.moveTo(843, 350, duration=0.1)
#pyautogui.click()

#pyautogui.typewrite('Azasdasd1', interval=0.05)

#pyautogui.moveTo(795, 428, duration=0.1)
#pyautogui.click()



confidence_threshold = 0.9
counter = 0
winCounter = 0
LossCounter = 0
Lost = 'Red.png' or "greenRon.png"
Won = 'blackRon.png'

RedCounter = 0




# DONT FORGET TO INSERT COORDINATES FOR INITIATION EDEN

while True:

    # first loop to scope out the right time to enter
    while True:
        if LossCounter >= Total:
            break
        elif pyautogui.locateOnScreen(Lost, confidence=confidence_threshold):
            LossCounter = LossCounter +1 
            print(LossCounter)
            time.sleep(2)
        elif pyautogui.locateOnScreen(Won, confidence=confidence_threshold):
            LossCounter=0
            print(LossCounter)
            time.sleep(2)



    # place initial bet
    time.sleep(1.5)
    PlaceBets = pyautogui.click(pyautogui.moveTo(365,719))

    while True:
        
        




        time.sleep(1.5)    
        PlaceBets =  pyautogui.click(pyautogui.moveTo(365,719))

        #time stamp
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")

        # Check for the first image
        
        Win = pyautogui.locateOnScreen(Won, confidence=confidence_threshold)


        if Win:
        
            counter += 1
            winCounter += 1
            print(f"W{winCounter} - [{counter}] @ {current_time}")
            # x,y = pyautogui.locateCenterOnScreen("blackDiamond.png")
            # x = x/2
            # y=y/2 
            time.sleep(3)      
            pyautogui.click(pyautogui.moveTo(365,719))
           
            #pyautogui.click()
         
         

            if winCounter >= GamesTillEnd:
                break
            
            # Runs the checker for reds to play again
            while True:
                if RedCounter ==Total-Games:
                    break
                elif pyautogui.locateOnScreen(Lost, confidence=confidence_threshold):
                    RedCounter+=1
                    time.sleep(2)
            continue

        
        # Check for the second image
        
        image_location = pyautogui.locateOnScreen(Lost, confidence=confidence_threshold)
        if image_location:
            print(2)
            counter += 1
            print(f"L - [{counter}] @ {current_time}")
            pyautogui.sleep(3)
            #clicks "repeat bet and then doubles"
            pyautogui.click(pyautogui.moveTo(592, 785, duration=0.1))

        else:
            if pyautogui.locateOnScreen("continuePlayingEden.png")!= None:
                pyautogui.click(pyautogui.locateCenterOnScreen("continuePlayingEden.png"))
                print("Continued")
        








