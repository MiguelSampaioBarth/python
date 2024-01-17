
import random
import os

opcao = ('y', 'n')
parar = True
ponto = 0

# -----------------------------------------------------PEDRA PAPEL OU TESOURA--------------------------------------------------------------

def executar_PPT():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Executando Pedra, Papel ou Tesoura.")

    while True :
        
        oponente = random.randint(1,3)
        entrada = input('\nescolha uma opção: \nPedra, Papel ou Tesoura\nCaso deseje sair, insira Y\n')
        player = entrada.lower()
        escolha = ('pedra', 'papel', 'tesoura')

        if player == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()


        if player in escolha :

            if oponente == 1 :
                oponente = 'pedra'
                os.system('cls' if os.name == 'nt' else 'clear')
                print('O oponente escolheu: ',oponente)
                print('Sua escolha foi: ',player)

                if player == oponente :
                    print('O resultado é: empate')
                    continue
                elif player == 'papel':
                    print ('O resultado é: ganhou')
                    continue
                else :
                    print ('O resultado é: perdeu')
                    continue
            

            elif oponente == 2 :
                oponente = 'papel'
                os.system('cls' if os.name == 'nt' else 'clear')
                print('O oponente escolheu: ',oponente)
                print('Sua escolha foi: ',player)

                if player == oponente :
                    print('O resultado é: empate')
                    continue
                elif player == 'pedra':
                    print ('O resultado é: perdeu')
                    continue
                else :
                    print ('O resultado é: ganhou')
                    continue


            elif oponente == 3:
                oponente = 'tesoura'
                os.system('cls' if os.name == 'nt' else 'clear')
                print('O oponente escolheu: ',oponente)
                print('Sua escolha foi: ',player)

                if player == oponente :
                    print('O resultado é: empate')
                    continue
                elif player == 'pedra':
                    print ('O resultado é: ganhou')
                    continue
                else :
                    print ('O resultado é: perdeu')
                    continue


            else:
                print('Comando inválido.')
                continue
        else:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print ('digite novamente!')
            continue

# ---------------------------------------------------------IMPAR OU PAR--------------------------------------------------------------------
        
def executar_IoP():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Executando Impar ou Par.")
    tentativas = 0
    escolhas = ('impar', 'par')
    

    while tentativas >= 0 :

        os.system('cls' if os.name == 'nt' else 'clear')
        IMP_PAR = str(input('Bem-vindo! Você gostaria de escolher qual opção?\nImpar / Par\nDeseja SAIR? digite Y/N\n'))
        minus = IMP_PAR.lower()

        if minus == 'y':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()

        elif minus not in escolhas :
            
            print ('digite novamente!')

        else :                
            
            while True:
                try:
                    variavel = int(input('Insira um número: '))

                    if variavel <= 1:
                        print('Digite um número maior que 1.')
                    else:
                        break  
                except ValueError:
                    print('Digite um número válido.')

            while True :

                    minus = IMP_PAR.lower()
                    num = random.randint(1,100)
                    selecao = ('impar','par')
                    while tentativas <=100 :
                        if minus in selecao:
                            os.system('cls' if os.name == 'nt' else 'clear')

                            if (num + variavel)%2 == 0 : #-----par-----

                                print ('você colocou ',variavel)
                                print ('\nO oponente colocou ',int(num))
                                print ('\no resultado é ',(num + variavel), ' ou seja par')


                                novo_jogo = input('deseja continuar?\n Y/N: ')
                                minus = novo_jogo.lower()
                                os.system('cls' if os.name == 'nt' else 'clear')

                                if minus not in opcao :
                                    while True:
                                        
                                        novo_jogo = input('Você digitou algo inválido.\ndeseja continuar?\n Y/N: ')
                                        minus = novo_jogo.lower()
                                            
                                        if minus != ('y','n') :
                                            
                                            os.system('cls' if os.name == 'nt' else 'clear')
                                            continue
                                        else:
                                           
                                            break
                                    

                                else :

                                    if minus == 'y' :
                                        
                                        executar_IoP()

                                    if minus == 'n' :
                                        
                                        main() 

                            else : #-----impar-----

                                os.system('cls' if os.name == 'nt' else 'clear')
                                
                                print ('você colocou ',variavel)
                                print ('\nO oponente colocou ',int(num))
                                print ('\no resultado é ',(num + variavel), ' ou seja impar')    

                                novo_jogo = input('deseja continuar?\n Y/N: ')
                                minus = novo_jogo.lower()
                                os.system('cls' if os.name == 'nt' else 'clear')

                                if minus not in opcao :
                                    print('Você digitou uma letra invalida')
                                    continue

                                else :

                                    if minus == 'y' :
                                        
                                        break

                                    if minus == 'n' :
                                        
                                        main() 

# -------------------------------------------------------------SLOTS-----------------------------------------------------------------------
    
def executar_Slo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Executando Slots.")

                    
    print ('Bem-vindo! Insira a quantidade de numeros que você gostaria de jogar:\n')

    numero = int(input(''))
    tentativas = 0

    while tentativas >= 0 :

        num1 = random.randint(1,numero)
        num2 = random.randint(1,numero)
        num3 = random.randint(1,numero)

    
        if numero >= 2 :
            os.system('cls' if os.name == 'nt' else 'clear')
            print('os numeros sorteados sao:\n',str(num1),str(num2),str(num3))
            
            if num1 == num2 == num3 :
                print('você ganhou o jackpot!\n\n')
                
                while tentativas <=100 :
                    novo_jogo = input('deseja continuar?\n Y/N: ')
                    minus = novo_jogo.lower()
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if minus not in opcao :
                        print('Você digitou uma letra invalida')
                        continue

                    else :

                        if minus == 'y' :
                            tentativas += 1
                            break

                        if minus == 'n' :
                            tentativas +=102
                            main()
                            
            else :
                while tentativas <=100 :
                    novo_jogo = input('deseja continuar?\n Y/N: ')
                    minus = novo_jogo.lower()
                    os.system('cls' if os.name == 'nt' else 'clear')

                    if minus not in opcao :
                        print('Você digitou uma letra invalida')
                        continue

                    else :

                        if minus == 'y' :
                            tentativas += 1
                            break

                        if minus == 'n' :
                            tentativas +=102
                            main()
                          
        else :
            print ('insira um numero maior que 1')
            executar_Slo()

# -------------------------------------------------------------FORCA-----------------------------------------------------------------------
            
# OBS_1: Este codigo foi o remake de outro projeto incompleto que eu havia feito. Foram feitas modificações para que funcionasse de maneira devida.
            
# OBS_2: Esta parte do codigo foi utilizado inteligencia artificial em partes. perguntei ao mesmo qual porcentagem era a modificação que havia feito.
# a resposta foi de 30% de alteração.
            

def executar_For():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Executando Forca.")

    palavra = ["python", "programação", "sushi", "codificação"]
    P_Oculta = random.choice(palavra)
    tentativas = 0
    palavra_final = '*' * len(P_Oculta)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('palavra atual:',palavra_final)
        letra = input('Insira uma letra: ')
        letra_chutada = letra.lower()

        if len(letra_chutada) == 1:
            if letra_chutada in P_Oculta:
                for i in range(len(P_Oculta)):
                    if P_Oculta[i] == letra_chutada:
                        palavra_final = palavra_final[:i] + letra_chutada + palavra_final[i+1:]

                if '*' not in palavra_final:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('A palvra secreta é', P_Oculta, '\n\nVocê conseguiu!\nVocê tentou um total de', tentativas, 'vezes.')

                    while tentativas <=100 :
                        novo_jogo = input('deseja continuar?\n Y/N: ')
                        minus = novo_jogo.lower()
                        os.system('cls' if os.name == 'nt' else 'clear')

                        if minus not in opcao :
                            print('Você digitou uma letra invalida')
                            continue

                        else :

                            if minus == 'y' :

                                palavra = ["python", "programação", "sushi", "codificação"]
                                P_Oculta = random.choice(palavra)
                                palavra_final = '*' * len(P_Oculta)
                                break

                            if minus == 'n' :
                                tentativas +=102
                                main()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                tentativas += 1
                print('insira outro caractere!')
                continue

            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            tentativas += 1
            print('Insira somente um caractere!')
            continue
        
# -------------------------------------------------------------MAIN------------------------------------------------------------------------

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        inicio = input('escolha uma dos jogos:\na: Pedra,Papel ou Tesoura.   \nb: Impar ou Par.  \nc: Slots.   \nd: forca   ')
        escolha = inicio.lower()
        comandos = {
            'a': executar_PPT,
            'b': executar_IoP,
            'c': executar_Slo,
            'd': executar_For,
            }

        if escolha in comandos:
            comandos[escolha]()

        else:
            print('Comando inválido.')
            continue

if __name__ == "__main__":
        main()
else : print('erro')   

