import os

lista = []
while True:
    opcao = input(f'Selecione uma opção \n [i]nserir [a]pagar [l]istar') 
    if opcao == 'i' or opcao == 'I':
        os.system('cls')
        item = input('Digite o item que deseja adicionar')
        lista.append(item)
    elif opcao == 'a' or opcao == 'A':
        if lista == []:
            print('Não há itens para apagar')
        else:
            indice_lista = int(input('Digite o índice do item que deseja apagar'))
            lista.pop(indice_lista)
    elif opcao == 'l' or opcao == 'L':
        os.system('cls')
        for indice, nome in enumerate(lista):
            print(indice, nome)
    else:
        print('Por favor, selecione uma opção válida')

