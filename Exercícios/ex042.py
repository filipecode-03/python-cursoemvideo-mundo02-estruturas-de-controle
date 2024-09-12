p1 = int(input('Primeiro segmento: '))
p2 = int(input('Segundo segmento: '))
p3 = int(input('Terceiro segmento: '))
eq = p1 == p2 and p3
iso = p1 == p2 or p1 == p3
es =  p1 != p2 and p3
if eq:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
elif iso:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')')