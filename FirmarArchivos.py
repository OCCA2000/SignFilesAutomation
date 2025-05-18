import pyperclip
import time
import pyautogui
import subprocess

def copyPaste(text,x,y):
    pyperclip.copy(text)
    button_x, button_y = x,y
    time.sleep(sleeping_time)
    pyautogui.click(button_x, button_y)

    time.sleep(sleeping_time)
    pyautogui.hotkey('ctrl', 'v')

sleeping_time = 0.5

subprocess.Popen(r"C:\Program Files\FirmaEC\firmador.exe")

time.sleep(10)

button_x, button_y = 150, 150
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

button_x, button_y = 150, 200
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

copyPaste(r"Z:\Trámites\CRISTIAN ALFREDO ORELLANA CEPEDA 1724589617-180724215922.p12",300,380)

time.sleep(sleeping_time)
pyautogui.hotkey('enter')

copyPaste("1375Probook",200, 280)

button_x, button_y = 400, 280
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

copyPaste(r"C:\Users\Cristian\Downloads\Archivos\CompraBono.pdf",300,380)

time.sleep(sleeping_time)
pyautogui.hotkey('enter')

button_x, button_y = 500, 560
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

time.sleep(5)

button_x, button_y = 1250, 560
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

button_x, button_y = 590, 135
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)
time.sleep(sleeping_time)
pyautogui.doubleClick(button_x, button_y)

pyperclip.copy("1")
time.sleep(sleeping_time)
pyautogui.hotkey('ctrl', 'v')

time.sleep(sleeping_time)
pyautogui.hotkey('enter')

button_x, button_y = 166, 254
time.sleep(sleeping_time)
pyautogui.moveTo(button_x, button_y)
pyautogui.scroll(-30000)

time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

button_x, button_y = 412, 370
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

button_x, button_y = 775, 575
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

time.sleep(5)

button_x, button_y = 650, 560
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)