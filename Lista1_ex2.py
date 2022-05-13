#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.


contador = 0
indice = 0
par = 0
impar = 0

while contador < 10:
    indice += 1
    n = int(input(f"Número {indice}:"))
    contador += 1
    
for i in range(n):
    if i %2 == 0:
        par += 1
    if i %2 != 0:
        impar += 1
        
print(f"A quantidade de números pares é {par}\nA quantidade de números impares é {impar}")
