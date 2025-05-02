cpf = input('Informe o seu CPF: ')
cpf = cpf.replace('.','',2) #funciona assim, objeto_string('valor a ser substituído', 'novo valor atribuído', quantidade de vezes que será substituido)
cpf = cpf.replace('-','')
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
contador_regressivo_2 = 11
lista = [] 
lista_str = []
total_numeros_1 = 0
total_numeros_2 = 0

for digito_1 in nove_digitos:
    lista_str.append(digito_1)
    digito_int = int(digito_1)
    lista.append(digito_int)    
    total_numeros_1 += digito_int * contador_regressivo_1
    contador_regressivo_1 -= 1
    
primeiro_digito = (total_numeros_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

lista_str.append(str(primeiro_digito))
lista.append(primeiro_digito)

for digito_2 in lista:
    total_numeros_2 += digito_2 * contador_regressivo_2
    contador_regressivo_2 -= 1    

segundo_digito = (total_numeros_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

lista_str.append(str(segundo_digito))
cpf_lista = list(cpf)

if lista_str == cpf_lista:
    print(f'O CPF {cpf}, é válido.')
else:
    print(f'O CPF {cpf}, não é válido.')