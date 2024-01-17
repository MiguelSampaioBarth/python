from pyautogui import *
import pyautogui
import time
import random

escolha = input('escolha a opção:\n1 = FOLHAS\nDigite qualquer outra coisa para CAVERNA.')

time.sleep(3) #tempo de espera.

# ADICIONAR : CLICK ALEATORIO

# numeros QUASE aleatório
num1 = random.randint(1,69)
num2 = random.randint(1,89)

x = random.randint(1, 2)  
y = random.randint(1, 2)
tempo_aleatorio = random.randint(280,340) # tempo parado
cliques_aleatorios = random.randint(1,5) # numero de cliques 


numero1 = (1 + (num1/100) + (num2/100) + (num2/100))/(1 + (num1/100))
numero2 = numero1/3
numero3 = numero1/4
numero4 = numero1/5
numero5 = numero1/6
numero6 = numero1/12
numero7 = numero1/13

def calmo () :
   
    with pyautogui.hold('shift'): # Para frente
        time.sleep(numero4)
        pyautogui.keyDown('w')
        time.sleep(numero5)
        if x >= 70 :
            pyautogui.keyUp('shift')
            time.sleep(numero2)
            if x >= 70 :
                pyautogui.click(clicks=1)
            pyautogui.keyDown('shift')
            time.sleep(numero7)    
        pyautogui.keyUp('w')
        time.sleep(numero2)
        if x >= 70 :
            pyautogui.click(clicks=1)
        pyautogui.keyUp('shift')
        time.sleep(numero3)

    with pyautogui.hold('shift'): # Para Trás
        time.sleep(numero3)
        pyautogui.keyDown('s')
        if x >= 70 :
            pyautogui.keyUp('shift')
            time.sleep(numero2)
            pyautogui.keyDown('shift')
            time.sleep(numero7)   

        pyautogui.keyUp('s')
        time.sleep(numero5)
        pyautogui.press('shift')
        time.sleep(numero3)

def apressado () :
            
    pyautogui.keyDown('w') # Para frente
    time.sleep(numero5)
    pyautogui.keyUp('w')
    if x == y :
        pyautogui.keyDown('shift')
        time.sleep(numero7)    
        pyautogui.keyUp('shift')

    time.sleep(numero2)

    time.sleep(numero3)

    if x == y :
        pyautogui.click(clicks=1)

    time.sleep(numero2)
    pyautogui.keyDown('s') # Para trás
    time.sleep(numero7)
    pyautogui.keyDown('shift')
    time.sleep(numero5)

    if x == y :
        pyautogui.click(clicks=1)

    time.sleep(numero4)
    pyautogui.keyUp('s')
    time.sleep(numero5)
    pyautogui.keyUp('shift')
    time.sleep(numero3)

while 1 :
    time.sleep(4)
        
    if escolha == '1' :
        apressado()
        continue
    else :
        if x >= 55 :
            apressado()
            continue
        else :
            apressado()
            continue
        
