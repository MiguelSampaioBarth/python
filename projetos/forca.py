import os

letra = 'a'
palavra = 'abacaxi'
letra_correta = ''
tentativas = 0
palavra_final = '*' * len(palavra)

while True:
    print('Palavra atual:', palavra_final)
    letra_chutada = input('Insira uma letra: ')

    if len(letra_chutada) == 1:
        if letra_chutada in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra_chutada:
                    palavra_final = palavra_final[:i] + letra_chutada + palavra_final[i+1:]

            if '*' not in palavra_final:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('A palavra secreta é', palavra, '\n\nVocê conseguiu!\nVocê tentou um total de', tentativas, 'vezes.')
                break
        else:
            tentativas += 1
            print('voce tentou um total de ',tentativas)
            break

        
    else:
        print('Insira somente um caractere!')

    os.system('cls' if os.name == 'nt' else 'clear')
