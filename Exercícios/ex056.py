sidade = 0
maior = 0
menor = 0
nomemaioridade = ''
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    sidade = sidade + idade
    media = sidade / 4
    if c == 'M':
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
            nomemaioridade = nome
        if idade < menor:
            menor = idade
print(f'A média de idade do grupo é de {media:.1f} anos')
#print('O homem mais velho tem {} anos e se chama {}')
#print('Ao todo são {} mulheres com menos de {} anos')