dias = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]
i = 0 
soma = 0
div = 0
soma2 = 0
maiordia2 = float ('-inf')
menordia2 = float('inf')

for dia in dias:
    if dia != 0 and dia > maiordia2:
        maiordia2 = dia

for dia in dias:
    if dia != 0 and dia < menordia2:
        menordia2 = dia

for i in range (len(dias)):
    if dias[i] > 0.0:
        soma += dias[i]
        div  += 1

media = soma/div

for i in range (len(dias)):
    if dias[i] > media:
        soma2 += 1

maiordia = max(dias)
menordia = min(dias)

print("Media do faturamento: " , media)
print("--Considerando o ZERO como menor valor de faturamento--")
print("Dia do maior faturamento: " , maiordia)
print("Dia do menor faturamento: " , menordia)
print("Soma dos dias com o faturamento maior que a média: " , soma2)
print("--Desconsiderando o ZERO como menor valor de faturamento--")
print("Dia do maior faturamento: " , maiordia2)
print("Dia do menor faturamento: " , menordia2)

