# -*- coding: utf-8 -*-

x = 1
y = 2

if x > y:
   print("x é maior") 
else:print("y é maior")

#Exercício 2

if x == y:
 print("é igual")
elif y > x:
  print("y é maior que x")

#Exercício 3 While

while x <10:
  print(x)
  x +=11 # mesma coisa que x = x+11


#Exercício 4 for

lista = [1,2,3,4,5]
lista2 = ["hello","world","!"]
lista3 = [0,"hello",7.8,True]

for i in lista3:
  print(i)

#Exercício 5
# Variavel i chegar até o 20 começando no 10 somando de 2 em 2
for i in range(10,20,2): 
  print(i)

#Exercício 6 Concatenar Strings

nome = "Mario"

sobrenome = "Alter"

concatenar = nome + " " + sobrenome

print(concatenar[0:11])
print (concatenar.upper()) # função upper coloca todos os caracteres em maísculo 