#from pynput.mouse import Button, Controller
#mouse = Controller()
import pyautogui, time
a=pyautogui
pyautogui.FAILSAFE = True
#simulates tab
def wa(sec):
    time.sleep(sec)
#function to reset resolution
def resetsolution():
    print(a.confirm(text='Did it Worked?',title='Run Again?', buttons=('Worked','Retry')))
    
def main():
    resetsolution()

if __name__ == '__main__':
    main()
