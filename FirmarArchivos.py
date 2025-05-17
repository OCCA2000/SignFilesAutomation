import pyperclip
import time
import pyautogui
import subprocess

sleeping_time = 2

subprocess.Popen(r"C:\Program Files\FirmaEC\firmador.exe")

time.sleep(5)

button_x, button_y = 150, 150
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

button_x, button_y = 150, 200
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

pyperclip.copy(r"Z:\Trámites\CRISTIAN ALFREDO ORELLANA CEPEDA 1724589617-180724215922.p12")

button_x, button_y = 300, 380
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

time.sleep(sleeping_time)
pyautogui.hotkey('ctrl', 'v')

time.sleep(sleeping_time)
pyautogui.hotkey('enter')

pyperclip.copy("1375Probook")

button_x, button_y = 200, 280
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

time.sleep(sleeping_time)
pyautogui.hotkey('ctrl', 'v')