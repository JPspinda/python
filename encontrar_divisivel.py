def encontrar_número_divisivel(a, b):
    lista = []
    
    for numero in range(a, b):
        if numero % 7 == 0 and numero % 5 != 0:
            lista.append(numero)
            
    return lista

divisivel = encontrar_número_divisivel(100, 200)
print(divisivel)