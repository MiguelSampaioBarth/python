from pyautogui import *
import pyautogui
import time
import random

escolha = input('escolha a opção:\n1 = FOLHAS\nDigite qualquer outra coisa para CAVERNA.\n')

time.sleep(3) #tempo de espera para iniciar a ação.

def shift():
    if x >= 70 :
        pyautogui.keyUp('shift')
        time.sleep(numero2)
        if x >= 70 :
            pyautogui.click(clicks=1)
        else:
            None
        pyautogui.keyDown('shift')
        time.sleep(numero7)
    else:
        None

def clique():
    if x == y :
        pyautogui.click(clicks=1)
    else:
        None

def Pedras () :
   
    with pyautogui.hold('shift'): # Para frente
        time.sleep(numero4)
        pyautogui.keyDown('w')
        time.sleep(numero5)
        shift()  

        pyautogui.keyUp('w')
        time.sleep(numero2)
        shift()
        
        time.sleep(numero3)

    with pyautogui.hold('shift'): # Para Trás
        time.sleep(numero3)
        pyautogui.keyDown('s')
        shift()

        pyautogui.keyUp('s')
        time.sleep(numero5)
        pyautogui.press('shift')
        time.sleep(numero3)

def Folhas () :
            
    pyautogui.keyDown('w') # Para frente
    time.sleep(numero5)
    pyautogui.keyUp('w')
    shift()

    time.sleep(numero2)
    pyautogui.keyDown('s') # Para trás
    time.sleep(numero7)
    pyautogui.keyDown('shift')
    time.sleep(numero3)
    clique()
    
    pyautogui.keyUp('s')
    time.sleep(numero3)
    pyautogui.keyUp('shift')
    time.sleep(numero6)

while 1 :

    num1 = random.randint(1,69)
    num2 = random.randint(1,89)

    numero1 = (1 + (num1/100) + (num2/100) + (num2/100))/(1 + (num1/100))
    numero2 = numero1/3
    numero3 = numero1/5
    numero4 = numero1/6
    numero5 = numero1/7
    numero6 = numero1/12
    numero7 = numero1/13

    tempo = random.randint(280,330) # tempo parado --------------------IMPORTANTE-------------------
    tempo_aleatorio = tempo + numero1

    cliques_aleatorios = random.randint(1,5) # numero de cliques

    x = random.randint(1, 10)  
    y = random.randint(1, 10)    

    time.sleep(tempo_aleatorio)
        
    if escolha == '1' :
        Folhas()
        continue
    else :
        if x >= 55 :
            Folhas()
            continue
        else :
            Pedras()
            continue
        
