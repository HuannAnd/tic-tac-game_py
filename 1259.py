n = int(input())
i = 0
pares = []
impares = []
while i < n:
   numero = int(input())
   if numero%2 == 0:
       pares.append(numero)
   else:
       impares.append(numero)
   i+=1
print(pares)
for index in range(len(pares)-1):
   if pares[index]>pares[index+1]:
       pares[index],pares[index+1] = pares[index+1],pares[index]


for index in range(len(impares)-1):
   if impares[index] > impares[index+1]:
       impares[index],impares[index+1] = impares[index+1],impares[index]


print(impares)
