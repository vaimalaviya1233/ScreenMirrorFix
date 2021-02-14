#from pynput.mouse import Button, Controller
#mouse = Controller()

import pyautogui, time, threading
a=pyautogui
pyautogui.FAILSAFE = True

#simulates wait
def wait(sec):
    time.sleep(sec)

#function to reset resolution
def resetsolution():
    resolution= a.size()
    a.hotkey('win','d')#minimizes any open windows for sefty protocol
    wait(0.5)
    a.hotkey('win','i')#opens Windows settings with hotkey(shortcut)
    wait(3)
    a.press('tab')#chooses System option
    a.press('enter')#presses enter to open system   settings
    wait(2)
    #navigates to menu according to resolution
    res=a.size()
    if (res[0] == 1366) and (res[1] == 768):
        a.press('tab',8)#goes to resolution dropdown menu
    elif (res[0] == 1360) and (res[1] == 768):
        a.press('tab', 8)#goes to resolution dropdown menu
    elif(res[0] == 1280) and (res[1] == 768):
          a.press('tab',8)#goes to resolution dropdown menu
    elif (res[0] == 1280) and (res[1] == 720) :
        a.press('tab',7)#goes to resolution dropdown menu
    elif (res[0] == 1024) and (res[1] == 768) :
        a.press('tab',8)#goes to resolution dropdown menu
    else :                    #elif (res[0] == 800) and (res[1] == 600):
        a.press('tab',7)#goes to resolution dropdown menu
        
    wait(1)
    a.press('enter',2,3)#choose other resolution than the recommended (3 seconds)
    a.press('tab')#navigates to keep res settings option when resolution changed
    wait(0.5)
    a.press('enter')#presses enter to keep resolution
    resolution = a.size()
    wait(1)

    res=a.size()
    if (res[0] == 1366) and (res[1] == 768) :
        a.press('tab',9)#Renavigates to resolution menu
    elif (res[0] == 1360) and (res[1] == 768) :
        a.press('tab', 9)#Renavigates to resolution menu
    elif (res[0] == 1280) and (res[1] == 768)  :
          a.press('tab',9)#Renavigates to resolution menu
    elif (res[0] == 1280) and (res[1] == 720) :
        a.press('tab',8)#Renavigates to resolution menu
    elif (res[0] == 1024) and (res[1] == 768) :
        a.press('tab',9)#Renavigates to resolution menu
    else :                  #elif (res[0] == 800) and (res[1] == 600):
        a.press('tab',8)#Renavigates to resolution menu

    wait(1)
    a.press('enter',2,3)#gives you only 3 seconds to choose recommended resolution
    wait(0.5)
    a.press('tab')#navigates to keep res settings
    a.press('enter')#presses enter to keep resolution which was recommended
    a.hotkey('win','i')#opens exsting settings window
    a.hotkey('alt','f4')#closes existing 
    
def main():
    pyautogui.FAILSAFE = True
    resetsolution()
    status=(a.confirm(text='Did it Worked?',title='Run Again?', buttons=['Worked','Retry']))
    if status == 'Retry':
        resetsolution()
    else:
        pyautogui.alert(text='Thanks',Title='See You Later', button='OK')
def failsure():
    a = True
    while (a==True):
        loc = pyautogui.position()
        if ((loc[0] == 0) or (loc[0] == 1365)):
            if((loc[1] == 0) or (loc[1] == 767)):
                exit()

failsafe =  threading.Thread(target=failsure)
chief = threading.Thread(target=main)

if __name__ == '__main__':
    failsafe.start()
    chief.start()
