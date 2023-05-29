import pandas as pd
from math import log

contadorN = 0
contadorY = 0

df = pd.read_csv('heart.csv')
df = df.drop(columns=['Cholesterol', 'ChestPainType', 'Oldpeak', 'ST_Slope', 'RestingBP', 'MaxHR', 'HeartDisease',
                      'RestingECG', 'FastingBS', 'HeartDisease', 'Age'])
df = df.dropna()

for i in range(0, 917):
    sexo = df["Sex"][i]

    if sexo == "F":
        df = df.drop(i)
    else:
        escolha = df["ExerciseAngina"][i]
        if escolha == "N":
            contadorN += 1
        else:
            contadorY += 1

list_class = [contadorN, contadorY]
list_porc = []

quant_result = contadorY + contadorN
quant_class = 2
entropia = 0

for i in range(0, quant_class):
    x = list_class[i] / quant_result
    list_porc.append(x)

for i in range(0, quant_class):
    porc = list_porc[i]
    x = log(porc) / log(2)
    entropia += porc * x

print("O resultado da entropia é: {:.4}".format(entropia * -1))
print("O valor máximo da entropia é: {:.4}".format(log(quant_class, 2)))
