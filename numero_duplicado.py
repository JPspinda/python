def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    
    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
            
        numeros_checados.add(numero)

    return primeiro_duplicado

lista_de_listas_de_inteiros = [
    [1, 3, 4, 1, 2, 5, 4, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 8],
    [1, 2, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 3, 5, 2, 4, 9, 0],
    [2, 3, 5, 6, 4, 1]
]
    
for lista in lista_de_listas_de_inteiros:
    print(lista, encontra_primeiro_duplicado(lista))