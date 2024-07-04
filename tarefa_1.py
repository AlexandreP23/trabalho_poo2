# # Tarefa 01:
# Você deverá desenvolver um programa em python onde o usuário deverá digitar o nome e a idade de 10 pessoas 
# e armazernar esses dados em um arquivo de texto (meu_arquivo.txt). O formato de gravação deverá ser conforme o exemplo:

# Maria, 22
# Ana Clara, 23
# Barbara Silva, 34
# Julio, 31
# Para essa tarefa você não deverá utilizar nenhuma estrutura de dados (lista, dicionário, etc).


def armazenar_dados(arquivo_pessoas):
    with open(arquivo_pessoas, 'w') as arquivo:
        for i in range(10):
            nome = input(f"Digite o nome da pessoa {i+1}: ")
            idade = input(f"Digite a idade da pessoa {i+1}: ")
            arquivo.write(f"{nome}, {idade}\n")

def main():
    armazenar_dados('meu_arquivo.txt')
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
    main()





