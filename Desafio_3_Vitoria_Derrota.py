# Desafio de exibir um rank com vitórias menos derrotas do Herói
# variáveis de entrada     -    input

print("&" * 50)
print("     Desafio Vitórias do Herói   ")
print("&" * 50)
print("\n")

nomeHeroi = input("Informe o nome do Herói: ")
vitoriasHeroi = int(input("Digite o número de vitórias: "))
derrotasHeroi = int(input("Digite o número de derrotas: "))
resultado = (vitoriasHeroi - derrotasHeroi)
cont = 0
# laço de repetição para executar o programa algumas vezes
#for cont in range (1,3):

# estrutura de decisão usando IF
if resultado <= 10:
    print(f"O {nomeHeroi} tem o saldo de {resultado} está no nível de Ferro")
elif resultado <= 20:
    print(f"O {nomeHeroi} tem o saldo de {resultado} está no nível de Bronze")
elif resultado <=50:
    print(f"O {nomeHeroi} tem o saldo de {resultado} está no nível de Prata")
elif resultado <=80:
    print(f"O {nomeHeroi} tem o saldo de {resultado} está no nível de Ouro")
elif resultado <=90:
    print(f"O {nomeHeroi} tem o saldo de {resultado} está no nível de Diamante")
elif resultado <=100:
    print(f"O {nomeHeroi} tem o saldo de {resultado} está no nível de Lendário")
else:
    print(f"O {nomeHeroi} tem o saldo de {resultado} está no nível de Imortal")

print("FIM \n")

print("&" * 50)

