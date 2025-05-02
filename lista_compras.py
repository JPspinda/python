import os
compras = []
print('Escolha uma das opções a seguir:')

while True:
    opcoes = input('[I]nserir    [A]pagar    [L]istar  [S]air: ')   
    
    if len(opcoes) == 0:
        os.system('cls')
        print('Escolha uma opção.')
        continue
    
    elif opcoes.lower() == 'i':
        os.system('cls')
        compra = input('Coloque um produto para adicionar na lista: ')
        compras.append(compra)
        print('Produto adicionado com sucesso!')
        continue
        
    elif opcoes.lower() == 'a':
        os.system('cls')
        if not compras:
            print('Lista Vazia.')
            continue 
        
        apagar = input('Escolha um índice para apagar: ')
        try:
            apagar_int = int(apagar)
            del compras[apagar_int]
            print('Produto deletado com sucesso!')
            continue
                
        except IndexError:
            print('Índice não existe na lista.')
        except ValueError:
            print('Por favor, digite um número.')
        except Exception:
            print('Erro Desconhecido.')
            
    elif opcoes.lower() == 'l':
        os.system('cls')
        for indice, nome in enumerate(compras):
            print(indice, nome)
            
    elif opcoes.lower() == 's':
        print('Saindo...')
        break