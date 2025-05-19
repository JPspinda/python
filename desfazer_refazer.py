def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        print()
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
        
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return
    
    tarefa = tarefas.pop() # tira o último item da lista e joga em uma variável
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    listar(tarefas)
    print()
    
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        return
    
    tarefa = tarefas_refazer.pop() # tira o último item da lista e joga em uma variável
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    listar(tarefas)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhum tarefa.')
        return
    
    tarefas.append(tarefa)
    listar(tarefas)
    print()

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    if tarefa == 'listar':
        listar(tarefas)
        continue
        
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue     
       
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue  
      
    else:
        adicionar(tarefa, tarefas)
        continue