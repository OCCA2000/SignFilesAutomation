import tkinter as tk
from tkinter import messagebox
import threading
import pyperclip
import time
import pyautogui
import subprocess
import shutil
import os

# Función principal que ejecuta el script de firmado
def run_script():
    try:
        def copyPaste(text,x,y):
            pyperclip.copy(text)
            button_x, button_y = x,y
            time.sleep(sleeping_time)
            pyautogui.click(button_x, button_y)
        
            time.sleep(sleeping_time)
            pyautogui.hotkey('ctrl', 'v')
        
        folder_path = r"Z:\Proyectos de programación\Python\Bolsa\Firmar\GUI\Entrada\\"
        subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
        
        for subfolder in subfolders:
            
            partial_path = subfolder.split('\\')
            stockbroker = partial_path[-1]
            
            input_path = fr"Z:\Proyectos de programación\Python\Bolsa\Firmar\GUI\Entrada\{stockbroker}\\"
            #input_path = r"S:\Entrada\\"
            
            files = os.listdir(input_path)
            
            sleeping_time = 1
            
            for file in files:
                
                subprocess.Popen(r"C:\Program Files\FirmaEC\firmador.exe")
                
                time.sleep(10)
            
                number_of_signatures = 0
            
                while number_of_signatures < 5:
                    
                    button_x, button_y = 150, 150  #Click en boton Archivo
                    time.sleep(sleeping_time)
                    pyautogui.click(button_x, button_y)
                    
                    button_x, button_y = 150, 200  #Click en boton Buscar Certificado
                    time.sleep(sleeping_time)
                    pyautogui.click(button_x, button_y)
                    
                    #copyPaste(r"Z:\Trámites\CRISTIAN ALFREDO ORELLANA CEPEDA 1724589617-180724215922.p12",300,380)
                    copyPaste(fr"Z:\Proyectos de programación\Python\Bolsa\Firmar\GUI\Firmas\{stockbroker}.p12",300,380)
                    
                    time.sleep(sleeping_time)
                    pyautogui.hotkey('enter')
                    
                    #copyPaste("JLVL881900va",200, 280)  #Coloca clave
                    copyPaste("1375Probook",200, 280)  #Coloca clave
                    
                    button_x, button_y = 400, 280   #Click en Buscar Documento
                    time.sleep(sleeping_time)
                    pyautogui.click(button_x, button_y)
                    
                    aux_file = file[:len(file)-4]+'-signed'*number_of_signatures+".pdf"  #Lee el archivo a firmar
                    
                    copyPaste(input_path+aux_file,300,380)  #Coloca el nombre del archivo a firmar en la caja de texto
                    
                    time.sleep(sleeping_time)
                    pyautogui.hotkey('enter')
                    
                    button_x, button_y = 500, 560   #Click en el boton Firmar
                    time.sleep(sleeping_time)
                    pyautogui.click(button_x, button_y) 
                    
                    time.sleep(5)
                    
                    button_x, button_y = 990, 416   #Click en boton Aceptar de la pantalla emergente de advertencia de tamaño de pagina
                    time.sleep(sleeping_time)
                    pyautogui.click(button_x, button_y)
                    
                    #pyautogui.hotkey('enter') #Click en boton Aceptar de la pantalla emergente de advertencia de tamaño de pagina
                    
                    button_x, button_y = 590, 135    #Se va a la caja de texto del numero de pagina
                    time.sleep(sleeping_time)
                    pyautogui.click(button_x, button_y)
                    time.sleep(sleeping_time)
                    pyautogui.doubleClick(button_x, button_y)   #DobleClick para seleccionar todo el contenido de la caja de texto de numero de pagina
                    
                    # #Bloque que escoge el numero de página a firmar
                    # if(number_of_signatures == 0):
                    #     button_x, button_y = 200, 250 #260     #Coordenada de la firma en la pagina 1 
                    #     pyperclip.copy("1")
                    # elif(number_of_signatures == 1):
                    #     button_x, button_y = 165, 360 #380     #Coordenada de la firma en la pagina 2 
                    #     pyperclip.copy("2")
                    # elif(number_of_signatures == 2):
                    #     button_x, button_y = 170, 155          #Coordenada de la firma en la pagina 3 
                    #     pyperclip.copy("3")
                    # elif(number_of_signatures == 3):
                    #     button_x, button_y = 225, 320 #340     #Coordenada de la firma en la pagina 4 
                    #     pyperclip.copy("4")
                    # elif(number_of_signatures == 4):
                    #     button_x, button_y = 165, 380 #400     #Coordenada de la firma en la pagina 5 
                    #     pyperclip.copy("5")
                    
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
                    pyautogui.hotkey('ctrl', 'v')   #Se pega el numero de página escogida en la caja de texto correspondiente1
                    
                    time.sleep(sleeping_time)
                    pyautogui.hotkey('enter')
                    
                    time.sleep(1)
                    pyautogui.moveTo(button_x, button_y)       #Se coloca en la coordenada correspondiente a cada pagina
                    
                    pyautogui.scroll(-30000)
                    
                    time.sleep(1)
                    pyautogui.click(button_x, button_y)        #Click en la coordenada donde se va a firmar
                    
                    time.sleep(sleeping_time)                  #Enter para colocar la firma
                    pyautogui.hotkey('enter')
                    
                    time.sleep(sleeping_time)
                    pyautogui.hotkey('enter')                  #Enter para estampar la firma
                    
                    time.sleep(5)
                    
                    button_x, button_y = 650, 560              #Click en el botón Salir
                    time.sleep(sleeping_time)
                    pyautogui.click(button_x, button_y)
                    
                    number_of_signatures += 1
                
                  #Fin del bucle de firmas
            
                button_x, button_y = 640, 10           #Clic en el boton "X" para cerrar la pantalla
                time.sleep(sleeping_time)
                pyautogui.click(button_x, button_y)
            
                time.sleep(3)
            
                shutil.move(input_path+file, "Z:/Proyectos de programación/Python/Bolsa/Firmar/GUI/Procesados/"+file)
            
                aux_file = file[:len(file)-4]+'-signed'*5+".pdf"
                shutil.move(input_path+aux_file, f"Z:/Proyectos de programación/Python/Bolsa/Firmar/GUI/Salida/{stockbroker}/Firmado_"+file)  #Renombra el archivo colocando al inicio la palabra Firmado
            
            #files = os.popen(f'dir /b /s "{input_path}*-signed*"').read().splitlines()  #Lee todos los archivos que tengan la palabra Signed
            files = os.listdir(input_path)
            
            for file in files:
                shutil.move(input_path+file,  "Z:/Proyectos de programación/Python/Bolsa/Firmar/GUI/FirmadosParciales/"+file)

        messagebox.showinfo("Éxito", "Proceso completado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

# Función que lanza el script en un hilo separado para no congelar la GUI
def start_process():
    button_run.config(state=tk.DISABLED)
    threading.Thread(target=lambda: [run_script(), button_run.config(state=tk.NORMAL)]).start()

# Configuración de la ventana
root = tk.Tk()
root.title("App Firmador Automático")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Haz clic para iniciar el proceso de firmado")
label.pack(pady=20)

button_run = tk.Button(root, text="Iniciar Firmado", command=start_process, width=20, height=2)
button_run.pack()

root.mainloop()
