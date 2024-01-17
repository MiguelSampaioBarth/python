lista =  []
novo_elemento = ' '
while True : 
    print('Escolha a opcao para suas compras: \n1 - Adicionar Item.\n2 - Exibir Lista\n3 - Excluir Item\n\n')
    entrada = input ('')
    if entrada == ('1'):
        while True :
            novo_elemento = input ('Adicione um item ou saia desta opcao com "*".\n')
            if novo_elemento != '*' :
                lista.append(novo_elemento)
                print (lista)
            elif novo_elemento == '*' :
                break
            else :  print ('\n ',lista, '\n')


    elif entrada == ('2'): 
        print ('\n',lista)


    elif entrada == ('3'): 
        print ('\n',lista)
        while True: 
            excluir_elemento = input('selecione o item que deseja apagar ou saia desta opcao com "-".\n')
            if excluir_elemento in lista :
                lista.remove(excluir_elemento)
                print (lista)
            elif excluir_elemento == '-':
                break
            else :
                print ('nao ha itens com essas caracteristicas')
                continue
    else :
        print ('invalido')