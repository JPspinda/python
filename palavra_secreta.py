import os #importa a função 'os'

palavra_secreta = input('Palavra Secreta: ')
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1 #cada vez que o laço é percorrido é adicionado mais 1
    
    if len(letra_digitada) > 1: #se tiver mais de uma letrairá voltar o laço
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada #concatena a letra digitada na letra acertada
        
    palavra_formada = '' #onde a palavra com os asteriscos será armazenada
    for letra_secreta in palavra_secreta: #o 'for' percorre a palavra
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta #se a letra secreta estiver na letra acertada, a letra secreta será concatenada na palavra formada
        else:
            palavra_formada += '*' #senão, o asterisco será concatenado
            
    print(f'Palavra formada: {palavra_formada}')
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou! Parabéns!')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        letras_acertadas = ''
        tentativas = 0
        #break