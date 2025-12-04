import pyautogui
import time

x = int(input('Digite 1:'))

time.sleep(3)

while x == 1:
    pyautogui.click(x=30, y=169)
    pyautogui.click(x=749, y=275)
    pyautogui.write("Testando script")
    pyautogui.click(x=975, y=547)
    pyautogui.click(x=1883, y=161)