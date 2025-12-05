class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo.lower()

    def atacar(self):
        ataques = {
            "mago": "magia",
            "guerreiro": "espada",
            "monge": "artes marciais",
            "ninja": "shuriken"
        }

        if self.tipo in ataques:
            ataque = ataques[self.tipo]
            print(f"O {self.tipo} atacou usando {ataque}")
        else:
            print("Tipo de herói desconhecido!")


def main():
    print("=== Criando seu herói ===")
    
    nome = input("Digite o nome do herói: ")
    idade = input("Digite a idade do herói: ")
    tipo = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ")

    heroi = Heroi(nome, idade, tipo)

    print("\n=== Resultado ===")
    print("\n =======================================")
    heroi.atacar()


# Executando o programa
main()
