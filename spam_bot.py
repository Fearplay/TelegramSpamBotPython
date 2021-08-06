import pyautogui #pip install pyautogui
'''
This program is for telegram on web. You need to login into it and then use this program.
'''
sentence1 ="Hello"
sentence2 ="World!"
pyautogui.sleep(5) #5 seconds to move your mouse on position which you need.
print(pyautogui.position()) #This is needed for moveTo because not every monitor is same. 
pyautogui.sleep(5)#5 seconds to stop program if you need.

i = 0
while(i < 10): 
    pyautogui.moveTo(609, 183) #This is position of my mouse when I click on first group. Your position can be different. For that use 'pyautogui.position()'.
    pyautogui.click() #This will click by left mouse.
    pyautogui.sleep(2) #This is for not lagging
    pyautogui.moveTo(1263, 1354) #This is position of my mouse when I click on message. Your position can be different. For that use 'pyautogui.position()'.
    pyautogui.click() #This will click by left mouse.
    pyautogui.write(sentence1) #This will write your sentence number one.
    pyautogui.hotkey('Shift', 'Enter') #This will click shift + enter which will create new line under your first sentence.
    pyautogui.write(sentence2) #This will write your sentence number two.
    pyautogui.hotkey('Enter') #This will send message
    pyautogui.sleep(2) #This is for not lagging


    pyautogui.moveTo(609, 285)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.moveTo(1263, 1354)
    pyautogui.click()
    pyautogui.write(sentence1)
    pyautogui.hotkey('Shift', 'Enter')
    pyautogui.write(sentence2)
    pyautogui.hotkey('Enter')
    pyautogui.sleep(2)
    i+=1 #This will ensure that the cycle is not endless
    