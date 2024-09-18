op = [1, 2, 3, 4, 5]
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while op != 5:
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        soma = v1 + v2
        print(f'A soma entre {v1} + {v2} é {soma}')
        print('=-=' * 10)
    elif op == 2:
        soma = v1 * v2
        print(f'O resultado de {v1} x {v2} é {soma}')
    elif op == 3:
        if v1 > v2:
            print(f'Entre {v1} e {v2} o maior valor {v1}')
        if v2 > v1:
            print(f'Entre {v1} e {v2} o maior valor {v2}')
    elif op == 
print('saiu do programa')