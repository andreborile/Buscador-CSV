import csv
import json

resultados = []

def buscar(termo_de_busca, coluna):
    with open('projeto_LP_tweets_2022.csv', 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            if termo_de_busca.lower() in linha[coluna].lower():
                resultados.append({
                    'data': linha['date'],
                    'conteudo': linha['content'],
                    'assunto': linha['subject']
                })
            print(f'{linha["date"]}  |  {linha["content"]}  |  {linha["subject"]}')

def salvar(arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo_json:
        json.dump(resultados, arquivo_json, indent=4)

# função para buscar tweets por data
def buscar_por_data():
    data = input('Digite a data no formato "AAAA-MM-DD": ')
    buscar(data, 'date')

# função para buscar tweets por termo
def buscar_por_termo():
    termo = input('Digite o termo de busca: ')
    buscar(termo, 'content')

# função para buscar tweets por assunto
def buscar_por_assunto():
    assunto = input('Digite o assunto de busca: ')
    buscar(assunto, 'subject')

# menu principal
while True:
    print('\nBoas vindas ao nosso sistema:\n')
    print('1 - Buscar tweets por data')
    print('2 - Buscar tweets por termo')
    print('3 - Buscar tweets por assunto')
    print('4 - Salvar resultado da busca')
    print('5 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        buscar_por_data()
    elif opcao == '2':
        buscar_por_termo()
    elif opcao == '3':
        buscar_por_assunto()
    elif opcao == '4':
        salvar('resultado_da_busca.json')
        print('Arquivo salvo como "resultado_da_busca.json"')
    elif opcao == '5':
        print('Saindo do programa. Até mais!')
        break
    else:
        print('Opção inválida. Escolha uma opção de 1 a 5.')