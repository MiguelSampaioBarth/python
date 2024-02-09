import keyboard as key
import pyautogui as py
import random
import time

def programa():
    
    while True:
        if key.read_key() == 'down' :
                        
                iniciar_programa()
        
        

def iniciar_programa():

    num1 = random.randint(1, 69)
    num2 = random.randint(1, 89)

    numero1 = (1 + (num1/79) + (num2/68) + (num2/89))/(1 + (num1/50))/2
    numero2 = (numero1 + numero1/2)/4
    numero3 = numero1/8
    numero4 = numero1/7
    tempo = numero1

    py.press('t')
    time.sleep(numero2)

    py.write('/pets', interval=numero3)
    time.sleep(numero4)

    py.press('enter')
    time.sleep(tempo)
    
    x = py.locateOnScreen(r'C:\Users\Mikes\OneDrive\Documentos\GitHub\python\afk_minecraft\pet\dev.png', confidence=0.7) # modificar o path da imagem
   
    if x:
        centrox = x.left + x.width /2
        centroy = x.top + x.height /2

        py.moveTo(centrox, centroy , duration= numero2)
        py.click()

programa()



