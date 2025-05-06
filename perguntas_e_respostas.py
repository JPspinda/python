import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '4', '5'],
        'Resposta': '4',
    },   
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',  
    }  
]
pontuacao = 0

for indice, dicionario in enumerate(perguntas):
    for chave, valor in perguntas[indice].items():
        if chave == 'Opções':
            for numero, resposta in enumerate(perguntas[indice]['Opções']):
                print(f'{numero}) {resposta}')
                
        elif chave == 'Resposta':
            continue
        
        else:
            print(f'\n{chave}: {valor}')
            
    resposta = input('Qual a sua resposta? ')  
    
    if resposta == dicionario['Resposta']:
        print('Resposta correta!')
        pontuacao += 1
        
    else:
        print('Resposta errada!')
        
os.system('cls')
print(f'\nSua pontução: {pontuacao}')

if pontuacao == 0:
    print('Precisa melhorar...')
    
elif pontuacao == 1 or pontuacao == 2:
    print('Não foi tão mal!')
    
else:
    print('Uau! Parabéns, você conseguiu a pontuação máxima!')