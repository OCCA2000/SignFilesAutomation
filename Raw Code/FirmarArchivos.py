import pyperclip
import time
import pyautogui
import subprocess
import shutil
import os

def copyPaste(text,x,y):
    pyperclip.copy(text)
    button_x, button_y = x,y
    time.sleep(sleeping_time)
    pyautogui.click(button_x, button_y)

    time.sleep(sleeping_time)
    pyautogui.hotkey('ctrl', 'v')

input_path = r"Z:\Proyectos de programación\Python\Bolsa\Firmar\Entrada\\"

files = os.listdir(input_path)

sleeping_time = 1

signature_writer = subprocess.Popen(r"C:\Program Files\FirmaEC\firmador.exe")

time.sleep(10)

for file in files:

    number_of_signatures = 0

    while number_of_signatures < 5:
        
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
        
        aux_file = file[:len(file)-4]+'-signed'*number_of_signatures+".pdf"
        
        copyPaste(input_path+aux_file,300,380)
        
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
        
        if(number_of_signatures == 0):
            button_x, button_y = 165, 240 #260
            pyperclip.copy("1")
        elif(number_of_signatures == 1):
            button_x, button_y = 165, 360 #380
            pyperclip.copy("2")
        elif(number_of_signatures == 2):
            button_x, button_y = 170, 160
            pyperclip.copy("3")
        elif(number_of_signatures == 3):
            button_x, button_y = 225, 320 #340
            pyperclip.copy("4")
        elif(number_of_signatures == 4):
            button_x, button_y = 170, 380 #400
            pyperclip.copy("5")
    
        time.sleep(sleeping_time)
        pyautogui.hotkey('ctrl', 'v')
        
        time.sleep(sleeping_time)
        pyautogui.hotkey('enter')
        
        time.sleep(1)
        pyautogui.moveTo(button_x, button_y)
        
        pyautogui.scroll(-30000)
        
        time.sleep(1)
        pyautogui.click(button_x, button_y)
        
        time.sleep(sleeping_time)
        pyautogui.hotkey('enter')
        
        time.sleep(sleeping_time)
        pyautogui.hotkey('enter')
        
        time.sleep(5)
        
        button_x, button_y = 650, 560
        time.sleep(sleeping_time)
        pyautogui.click(button_x, button_y)
        
        number_of_signatures += 1
    

button_x, button_y = 640, 10
time.sleep(sleeping_time)
pyautogui.click(button_x, button_y)

time.sleep(3)

for file in files:
    aux_file = file[:len(file)-4]+'-signed'*5+".pdf"
    shutil.move(input_path+aux_file, "Salida/Firmado_"+file)

files = os.popen(f'dir /b /s "{input_path}*-signed*"').read().splitlines()

for file in files:
    print("Eliminando "+file)
    os.remove(file)