'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

print("TABUADA DE MULTIPLICAÇÃO | 1 A0 10")
num = int(input("Número: "))
c = 0 
while num < 0 or num > 10:
    print("Inválido.")
    num = int(input("Número: "))
for i in range (10):
    c += 1
    produto = num * c
    print(f'{num} * {c} = {produto}')
