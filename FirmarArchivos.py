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

number_of_signs = 0

while number_of_signs < 6:
    
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
    
    copyPaste(fr"C:\Users\Cristian\Downloads\Archivos\CompraBono{'-signed'*number_of_signs}.pdf",300,380)
    
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
    
    if(number_of_signs == 0):
        button_x, button_y = 165, 260
        pyperclip.copy("1")
    elif(number_of_signs == 1):
        button_x, button_y = 165, 380
        pyperclip.copy("2")
    elif(number_of_signs == 2):
        button_x, button_y = 170, 160
        pyperclip.copy("3")
    elif(number_of_signs == 3):
        button_x, button_y = 225, 340
        pyperclip.copy("4")
    elif(number_of_signs == 4):
        button_x, button_y = 170, 400
        pyperclip.copy("5")
    elif(number_of_signs == 5):
        button_x, button_y = 350, 210
        pyperclip.copy("6")

    time.sleep(sleeping_time)
    pyautogui.hotkey('ctrl', 'v')
    
    time.sleep(sleeping_time)
    pyautogui.hotkey('enter')
    
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
    
    number_of_signs += 1