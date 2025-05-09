def contar_caracteres(string):
    letras = 0
    numero = 0
    
    for caracter in string:
        if caracter == ' ':
            continue
        try:
            int(caracter)
            numero += 1
        except ValueError:
            letras+= 1
            
    return f'Quantidade de letras: {letras} / Quantidade de número: {numero}'

quantidade = contar_caracteres('Olá mundo 123')
print(quantidade)