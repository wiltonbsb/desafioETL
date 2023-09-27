import csv
dados = 'SDW2023.csv'
with open(dados, newline='') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)

    for linha in leitor_csv:
        name = linha['nome']
        print(f'Obrigado por ser nosso cliente {name}!')