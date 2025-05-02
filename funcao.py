def mult(*args):
    total = 1
    for numero in args:
        total = total * numero
    return total

def par_impar(num):
    num_int = int(num)
    
    if num_int % 2 == 0:
        return f'{num} é um número par.'
    else:
        return f'{num} é um número ímpar.'
    
mult = mult(2, 2, 2)
numero = par_impar(input('Digite um número: '))
print(mult)
print(numero)