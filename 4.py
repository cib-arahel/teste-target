soma = 0

vetor = []

estados = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53 ]


for i in range(len(estados)):
    soma += estados[i]

for i in range(len(estados)):
    porc = (estados[i]/soma)*100
    vetor.append(porc)

sp = vetor[0]
rj = vetor[1]
mg = vetor[2]
es = vetor[3]
outros = vetor[4]

print("%SP: " , sp)
print("%RJ: " , rj)
print("%MG: " , mg)
print("%ES: " , es)
print("%OUTROS: " , outros)


