from pyautogui import *
import pyautogui
import time
import os



def botao ():
    while True :
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você terá 10 segundos até a automoção inicicar DEPOIS DE INICAR para poder trocar de tela.')
        escolha = input('insira a opção:\n1 = somente uma letra\n2 = SHIFT + (letra desejada) + (letra desejada)')

        if escolha == '1' :
            while True :
                TECLA = input('insira O UNICO CARACTERE para realizar a ação:')

                os.system('cls' if os.name == 'nt' else 'clear')
                print ('A automoção encerra automaticamente a cada 20 min para evitar travamentos e punições do usuario.')
                print('VOCÊ TEM 10 SEGUNDOS PARA TROCAR DE TELA!\nOBS: não fará mal ao computador. Mas caso perca o timing, terá que reiniciar a ação.')
                
                time,sleep(10) # TEMPO PARA O USUARIO
                
                pyautogui.keyDown(TECLA) 
                
                time.sleep(1200) # 20 min
                
                break

        elif escolha == '2' :
            TECLA = input('insira o PRIMEIRO caractere para realizar a ação:')
            TECLA2 = input('insira o SEGUNDO caractere para realizar a ação:')
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('A automoção encerra automaticamente a cada 20 min para evitar travamentos e punições do usuario.')
            print('VOCÊ TEM 10 SEGUNDOS PARA TROCAR DE TELA!\nOBS: não fará mal ao computador. Mas caso perca o timing, terá que reiniciar a ação.')
            
            time,sleep(10) # TEMPO PARA O USUARIO

            pyautogui.keyDown('shift')
            pyautogui.keyDown(TECLA)
            pyautogui.keyDown(TECLA2)

            time.sleep(1200) # 20 min
            
            break

        else :
            print ('ERRO\nTente novamente em 3 segundos.')
            time.sleep(3)
            botao()

# Ação obrigatória para o sistema iniciar.
if True:
    botao()
