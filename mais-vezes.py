frase = input('Escreva uma frase: ')

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes =  ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_aparecer_mais_vezes_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if apareceu_mais_vezes < qtd_aparecer_mais_vezes_atual:
        apareceu_mais_vezes = qtd_aparecer_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{apareceu_mais_vezes}x'
)