import csv
import json
import os

class GerenciadorTweets:
    def __init__(self, caminho_csv):
        self.caminho_csv = caminho_csv
        self.resultados = []

    def buscar(self, termo_de_busca, coluna):
        """Busca um termo em uma coluna específica do CSV."""
        if not os.path.exists(self.caminho_csv):
            print(f"\n[ERRO] Arquivo '{self.caminho_csv}' não encontrado!")
            return

        termo_de_busca = termo_de_busca.strip().lower()
        encontrou = False
        
        # 'utf-8-sig' resolve problemas de caracteres ocultos no início do arquivo
        with open(self.caminho_csv, 'r', encoding='utf-8-sig') as arquivo_csv:
            # Detecta automaticamente se o separador é vírgula ou ponto e vírgula
            dialeto = csv.Sniffer().sniff(arquivo_csv.read(1024))
            arquivo_csv.seek(0)
            leitor = csv.DictReader(arquivo_csv, dialect=dialeto)

            for linha in leitor:
                # Limpa espaços nos nomes das colunas
                linha = {k.strip().lower(): v for k, v in linha.items() if k}
                
                valor_coluna = linha.get(coluna.lower(), "")
                if termo_de_busca in valor_coluna.lower():
                    self.resultados.append({
                        'data': linha.get('date', 'N/A'),
                        'conteudo': linha.get('content', 'N/A'),
                        'assunto': linha.get('subject', 'N/A')
                    })
                    encontrou = True
        
        if encontrou:
            print(f"\n✅ Busca concluída! {len(self.resultados)} itens no total acumulado.")
        else:
            print(f"\n⚠️ Nenhum resultado novo para '{termo_de_busca}'.")

    def salvar_json(self, nome_arquivo):
        """Salva a lista de resultados em um arquivo JSON."""
        if not self.resultados:
            print("\n[AVISO] Não há resultados para salvar. A lista está vazia.")
            return

        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump(self.resultados, f, indent=4, ensure_ascii=False)
            print(f"\n💾 Sucesso! Arquivo '{nome_arquivo}' gerado com {len(self.resultados)} registros.")
        except Exception as e:
            print(f"\n[ERRO] Falha ao salvar: {e}")

    def limpar_resultados(self):
        self.resultados = []
        print("\n🧹 Memória de busca limpa.")

# --- Interface de Menu ---

def menu():
    # Inicializa o gerenciador com o nome do seu arquivo
    app = GerenciadorTweets('projeto_LP_tweets_2022.csv')

    io_opcoes = {
        '1': ('data', 'date'),
        '2': ('termo', 'content'),
        '3': ('assunto', 'subject')
    }

    while True:
        print('\n' + '='*30)
        print(' SISTEMA DE BUSCA DE TWEETS')
        print('='*30)
        print('1 - Buscar por DATA (AAAA-MM-DD)')
        print('2 - Buscar por CONTEÚDO (Termo)')
        print('3 - Buscar por ASSUNTO')
        print('4 - Salvar busca em JSON')
        print('5 - Limpar buscas anteriores')
        print('6 - Sair')
        
        opcao = input('\nEscolha uma opção: ')

        if opcao in io_opcoes:
            label, coluna = io_opcoes[opcao]
            termo = input(f'Digite o {label} de busca: ')
            app.buscar(termo, coluna)
        
        elif opcao == '4':
            app.salvar_json('resultado_da_busca.json')
        
        elif opcao == '5':
            app.limpar_resultados()
            
        elif opcao == '6':
            print('Saindo... Até logo!')
            break
        else:
            print('Opção inválida!')

if __name__ == "__main__":
    menu()