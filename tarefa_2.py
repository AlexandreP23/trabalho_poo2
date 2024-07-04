# Tarefa 02:
# Você deverá desenvolver um programa em python que leia o arquivo anterior, e coloque esses dados em uma lista de objetos instanciados da classe a baixo (lst_teste = []):
# class Teste:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# Após ter populado a lista, mostre um relatório com o seguinte formato:
# ===== Meu Relatório =====
# Maria................. 22
# Ana Clara............. 23
# Barbara Silva......... 34
# Julio................. 31
# ---------------Média: 27.5

# Após chame o professor para explicar o código!

class Teste:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


def ler_dados(relatorio):
    lst_teste = []
    with open(relatorio, 'r') as arquivo:
        for linha in arquivo:           
            dados = linha.strip().split(', ')
            nome = dados[0]
            idade = int(dados[1])            
            objeto_teste = Teste(nome, idade)
            lst_teste.append(objeto_teste)
    return lst_teste


def calcular_media_idades(lst_teste):
    if not lst_teste:
        return 0
    total_idades = sum(teste.idade for teste in lst_teste)
    media = total_idades / len(lst_teste)
    return media


def gerar_relatorio(lst_teste):
    print("===== Meu Relatório =====")
    for teste in lst_teste:
        print(f"{teste.nome:.<20} {teste.idade}")
    media = calcular_media_idades(lst_teste)
    print(f"---------------Média: {media:.1f}")

def main():
    
    relatorio = 'meu_arquivo.txt'    
  
    lst_teste = ler_dados(relatorio)    
    
    gerar_relatorio(lst_teste)

if __name__ == "__main__":
    main()
