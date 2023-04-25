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
pyautogui.sleep(3)

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Generate a random x and y coordinate within the screen size
x_coord = random.randint(0, screen_width)
y_coord = random.randint(0, screen_height)

# Move the mouse to the random coordinate and click it
pyautogui.moveTo(1285, 175, duration=0.1)
pyautogui.click()

pyautogui.moveTo(800, 290, duration=0.1)
pyautogui.click()

pyautogui.typewrite('', interval=0.05)

pyautogui.moveTo(843, 350, duration=0.1)
pyautogui.click()

pyautogui.typewrite('', interval=0.05)

pyautogui.moveTo(795, 428, duration=0.1)
pyautogui.click()

pyautogui.sleep(2)

#"games"
pyautogui.moveTo(780, 308, duration=0.1)
pyautogui.click()

pyautogui.sleep(3)

pyautogui.moveTo(333, 247, duration=0.1)
pyautogui.click()

pyautogui.sleep(3)

pyautogui.moveTo(92, 680, duration=0.1)
pyautogui.click()

pyautogui.sleep(3)

pyautogui.moveTo(450, 400, duration=0.1)
pyautogui.click()

pyautogui.sleep(2)

pyautogui.scroll(-20)

pyautogui.sleep(1)

pyautogui.moveTo(1235, 790, duration=0.1)
pyautogui.click()

pyautogui.sleep(8)

#pyautogui.moveTo(630, 190, duration=0.1)
#pyautogui.moveTo(630, 235, duration=0.1)
#pyautogui.click()

pyautogui.moveTo(312, 574, duration=0.1)
pyautogui.click()

pyautogui.moveTo(407, 490, duration=0.1)
pyautogui.click()

pyautogui.sleep(2)

confidence_threshold = 0.9
counter = 0



while True:
    
    #time stamp
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    
    # Check for the first image
    target_image = 'youWin.png'
    image_location = pyautogui.locateOnScreen(target_image, confidence=confidence_threshold)
    if image_location:
        counter += 1
        print(f"W - [{counter}] @ {current_time}")
        pyautogui.sleep(2)
        pyautogui.moveTo(312, 574, duration=0.1)
        pyautogui.click()

        pyautogui.moveTo(407, 490, duration=0.1)
        pyautogui.click()
        
        #makes sure the "you lost" function doesnt get excecuted right after
        time.sleep(8)

    # Check for the second image
    target_image = 'chips.png'
    image_location = pyautogui.locateOnScreen(target_image, confidence=confidence_threshold)
    if image_location:
        counter += 1
        print(f"L - [{counter}] @ {current_time}")
        pyautogui.sleep(1.5)
        #clicks "repeat bet and then doubles"
        pyautogui.moveTo(463, 574, duration=0.1)
        pyautogui.click()
        pyautogui.sleep(0.5)
        pyautogui.click()
        
        time.sleep(7)
       
