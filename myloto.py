import pyautogui
import random
import webbrowser
import time
from datetime import datetime

# List of random websites to choose from
websites = ['https://loteries.espacejeux.com/en/home']

# Open a random website from the list
webbrowser.open(random.choice(websites))

# Wait for the website to load
pyautogui.sleep(15)

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


while True:
    
    #time stamp
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    
    # Check for the first image
    target_image = 'black.png'
    image_location = pyautogui.locateOnScreen(target_image, confidence=confidence_threshold)
    if image_location:
        counter += 1
        winCounter += 1
        print(f"W{winCounter} - [{counter}] @ {current_time}")
        x,y = pyautogui.locateCenterOnScreen("blackDiamond.png")
        x = x/2
        y=y/2       
        pyautogui.moveTo(x,y)
        #pyautogui.click()
        time.sleep(0.5)
        #pyautogui.click()
        #makes sure the "you lost" function doesnt get excecuted right after
        time.sleep(8)
        
        if winCounter >= 30:
            break

    # Check for the second image
    target_image = 'PYB.png'
    image_location = pyautogui.locateOnScreen(target_image, confidence=confidence_threshold)
    if image_location:
        counter += 1
        print(f"L - [{counter}] @ {current_time}")
        pyautogui.sleep(1.5)
        #clicks "repeat bet and then doubles"
        pyautogui.moveTo(463, 574, duration=0.1)
        #pyautogui.click()
        pyautogui.sleep(0.5)
        #pyautogui.click()
        
        time.sleep(6.5)
       

        

