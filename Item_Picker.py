from pynput import keyboard as kb
from python_imagesearch.imagesearch import *
import pyscreenshot as pss
import time
import numpy

def GetWindowTopLeft(window):
    return (window.top,window.left)

def on_press(key):
    try:
        if key == kb.Key.esc:
            print("found an escape")
        if key.char == "e":
            window = pyautogui.getWindowsWithTitle("Risk of Rain 2")[0]
            if(window.isActive):#if the window isn't active, don't slow down typing
                method = cv2.TM_SQDIFF_NORMED
                screenshot = pyautogui.screenshot(region=(window.left+(window.width/3),window.top+(window.height/3),window.width/3,window.height/3))
                large_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
                small_image = cv2.imread("./Items/Backup_Magazine.png") #Subject to change based on the item we want to find
                h, w, colorDepth = small_image.shape
                
                result = cv2.matchTemplate(large_image, small_image, method)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                threshold = 0.995
                if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                    top_left = min_loc
                else:
                    top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)

                cv2.rectangle(large_image,top_left, bottom_right, 255, 2)
                
        
    except Exception as e:
        if(e != "'Key' object has no attribute 'char'"):
            print(e)
        return 0
    
# ...or, in a non-blocking fashion:
listener = kb.Listener(
    on_press=on_press,
    on_release=None)
listener.start()

hold = input("Press enter to close the script!")