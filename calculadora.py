while True:
    numero_1 = input('Coloque um número: ')
    numero_2 = input('Coloque outro número: ')

    valida_numero = False
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        valida_numero = True
    except:
        print('Coloque um número válido.')
        continue

    if valida_numero:
        operador = input('Informe um operador (+, -, *, /): ')
        operador_valido = '+-*/'

        if len(operador) > 1:
            print('Coloque apenas 1 operador.')
            continue

        if operador not in operador_valido:
            print('Informe um operador válido.')
            continue

        if operador == '+':
            soma = numero_1 + numero_2
            print(f'A soma de {numero_1} e {numero_2} é {soma}')
        
        elif operador == '-':
            sub = numero_1 - numero_2
            print(f'A subtrção de {numero_1} e {numero_2} é {sub}')

        elif operador == '*':
            mult = numero_1 * numero_2
            print(f'A multiplicação de {numero_1} e {numero_2} é {mult}')

        elif operador == '/':
            divisao = numero_1 / numero_2
            print(f'A divisão de {numero_1} e {numero_2} é {divisao}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')# transforma as letras em minúsculo, vê se a string começa com determinada letra, retorna um tipo bool

    if sair:
        break
    