import pyautogui
import os
import time

time.sleep(10)

step = 14
jedna_kratka_ma_x_piksele = 32
mapa_ma_x_kratek = 252
piksel_w_prawym_lewym_rogu = [15,138]

for y in range(18):
    for x in range(18):
        myScreenshot = pyautogui.screenshot()
        myScreenshot_name = str(x).rjust(2, "0") + str(y).rjust(2, "0") + ".png"
        myScreenshot.save(os.path.join("screenshots", myScreenshot_name))
        for i in range(step):
            pyautogui.press('right')
    for i in range(step):
        pyautogui.press('down')
    for i in range(mapa_ma_x_kratek):
        pyautogui.press("left")



