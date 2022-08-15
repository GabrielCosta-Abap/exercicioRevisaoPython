nomes = ['banana', 'maçã', 'laranja']
precos = ['1.54', '2.50', '3.00']
quantidades = [8, 10, 3]

def imprimeProduto(index):
    print(f'Nome: { nomes[index] }')
    print(f'Preço: { precos[index] }')
    print(f'Quantidade: { quantidades[index] }')

def removeProduto(index):
    try:
        nomes.pop(index)
        precos.pop(index)
        quantidades.pop(index)
        print('Produto removido com sucesso!')
    except:
        print('Produto não encontrado')

while True:
    opcao = input('''Menu:
        1 - Imprimir Produto
        2 - Remover Produto
        3 - Exibir listas
        4 - Finalizar programa
     ''')

    if opcao == '1':
        try:
            imprimeProduto(int(input('Digite a posição do produto: ')))
        except:
            print('Produto não encontrado.')
    elif opcao == '2':
        try:    
            removeProduto(int(input('Qual produto você deseja remover? ')))
        except:
            print('Produto não encontrado.')
    elif opcao == '3':
        print(nomes)
        print(precos)
        print(quantidades)
    elif opcao == '4':
        break
    else:
        print('Opção não encontrada')
