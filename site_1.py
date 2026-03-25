empresas = [
    {"nome": "AlphaTech", "setor": "Tecnologia", "receita": 120, "lucro": 25},
    {"nome": "BioHealth", "setor": "Saúde", "receita": 95, "lucro": 18},
    {"nome": "GreenEnergy", "setor": "Energia", "receita": 150, "lucro": 35},
]
total = 0

# soma do total final de lucros
for e in empresas:
    totalfinal = total + e["lucro"]

# calcula porcentagem
for e in empresas:
    porcentagem = (e["lucro"] / totalfinal) * 100
    print(e["nome"], "-", round(porcentagem, 2), "%")

import matplotlib.pyplot as plt

nome = []
lucro = []

for i in empresas: 
    nome.append(i["nome"])
    lucro.append(i["lucro"])

plt.title("Lucro final")
plt.pie(lucro, labels=nome, autopct="%1.2f%%")
plt.show()