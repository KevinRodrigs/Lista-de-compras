try:
    cpf = input('Informe o número do CPF') 
    nove_digitos = cpf[:9]
    contador_1 = 10

    resultado = 0
    for digito_1 in nove_digitos:
        resultado += int(digito_1) * contador_1
        contador_1 -= 1
    digito_1 = (resultado * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + 'digito_1'
    contador_2 = 11

    resultado_2 = 0
    for digito_2 in dez_digitos:
        resultado_2 += int(digito_1) * contador_2
        contador_2 -= 1
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_calculado == cpf:
        print(f'O CPF {cpf} é válido!!!')
    else:
        print(f'O CPF {cpf} não é válido!!!')
except:
    print('utilize apenas números inteiros')