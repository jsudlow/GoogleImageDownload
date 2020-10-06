from pyautogui import press,typewrite,keyDown,keyUp,click
import webbrowser
import time
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
webbrowser.get(chrome_path).open_new("images.google.com")
crosswalk_count = 0
time.sleep(3)
typewrite('dog')
time.sleep(1)
press('enter')
time.sleep(1)
tabcount = 1



keyDown('ctrl')
press('f')
keyUp('ctrl')
typewrite('bbc')
press('esc')
press('tab')	
time.sleep(1)
press('enter')

for i in range(100):
  press('apps')
  for i in range(6):
    press('down')
  press('enter')
  click(350,590)
  keyDown('ctrl')
  press('a')
  press('del')
  keyUp('ctrl')
  image_string = "dog_" + str(crosswalk_count)
  typewrite(image_string)
  keyDown('alt')
  press('s')
  keyUp('alt')
  click(1845,180)
  time.sleep(1)
  crosswalk_count += 1





