def encontra_soma(array, resultado):
    for indice1, numero in enumerate(array):
        for indice2, number in enumerate(array):
            if indice1 == indice2:
                continue
            
            else:
                if array[indice1] + array[indice2] == resultado:
                    return f'Os índices do array para somar e dar o resultado {resultado} são: {indice1} e {indice2}'
                
    return f'Não há números que, somados, dão o resultado {resultado}'

lista = []
for i in range(10):
    numero = int(input('informe um número: '))
    lista.append(numero)

resultado = int(input('Dê um resultado: '))

print(encontra_soma(lista, resultado))