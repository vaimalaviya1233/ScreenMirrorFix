#from pynput.mouse import Button, Controller
#mouse = Controller()
import pyautogui
import time
a = pyautogui
pyautogui.FAILSAFE = True
# simulates wait


def wait(sec):
    time.sleep(sec)
# function to reset resolution


def resetsolution():
    resolution = a.size()
    a.hotkey('win', 'd')  # minimizes any open windows for sefty protocol
    wait(0.5)
    a.hotkey('win', 'i')  # opens Windows settings with hotkey(shortcut)
    wait(2)
    a.press('tab')  # chooses System option
    a.press('enter')  # presses enter to open system   settings
    wait(1)
    # goes to resolution dropdown menu
    a.press('tab', 8)
    wait(1)
    # choose other resolution than the recommended (3 seconds)
    a.press('enter', 2, 3)
    a.press('tab')  # navigates to keep res settings option when resolution changed
    wait(0.5)
    a.press('enter')  # presses enter to keep resolution
    resolution = a.size()
    wait(1)
    a.press('tab', 9)  # Renavigates to resolution menu
    wait(1)
    # gives you only 3 seconds to choose recommended resolution
    a.press('enter', 2, 3)
    wait(0.5)
    a.press('tab')  # navigates to keep res settings
    a.press('enter')  # presses enter to keep resolution which was recommended
    a.hotkey('win', 'i')  # opens exsting settings window
    a.hotkey('alt', 'f4')  # closes existing


def main():
    resetsolution()
    status = (a.confirm(text='Did it Worked?',
                        title='Run Again?', buttons=('Worked', 'Retry')))
    if status == 'Retry':
        resetsolution()


if __name__ == '__main__':
    main()

res=pyautogui.size
if (res[0] == 1366) and (res[1] == 768):
    a.press('tab', 8)