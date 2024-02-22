
#Importação da biblioteca que vamos usar
import pandas as pd 

#Usando try para tentar seguir o fluxo sem ter problemas com a seleção de arquivo
try:
    # #Usando pandas para ler um arquivo csv e transformar em DataFrame
    base_credit = pd.read_csv(r'C:\Users\alecsilva-ieg\OneDrive - Instituto Germinare\Área de Trabalho\PicPay\Artermis\Machine Learning e Data Science\Bases de dados\credit_data.csv')
    print("Arquivo carregado com sucesso!")

    #Printando os dez primeiros registros com a função head
    print('\033[30;44mDez primeiros registros:\033[m')
    print()
    print(base_credit.head(10))
    print()

    #Mostrando os oito últimos registros com a função head
    print('\033[30;42mOito últimos registros:\033[m')
    print()
    print(base_credit.tail(8))
    print()

    #Descrevendo tipo de dado de cada coluna e mais algumas informações
    print('\033[0;30;41mDescrição dos aspectos da tabela\033[m')
    print()
    print(base_credit.describe)
    print()

    #Vendo cliente com maior salário 
    print('\033[30;45mCliente com maior salário\033[m')
    print()

    #Eu puxei o maior número e, baseado na coluna de salário do DataFrame, eu comparo com o maior número para achar esse registro
    print(base_credit[base_credit['income'] #Indicando a coluna
                    >= 69995.685578])
    print()

    #Vendo clientes com menor dívida
    print('\033[30;46mCliente com menor dívida\033[m')
    print()

    #Eu puxei o menor número e, baseado na coluna de dívida do DataFrame, eu comparo com menor número para achar esse registro
    base_credit[base_credit['loan'] #Indicando coluna
                    <= 1.377630]
    #.
except FileNotFoundError:
    # Erro caso o arquivo não seja encontrado
    print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
except pd.errors.EmptyDataError:
    # Erro caso o arquivo esteja vazio
    print("Arquivo vazio. Por favor, forneça um arquivo CSV válido.")
except pd.errors.ParserError:
    # Erro ao analisar o arquivo
    print("Erro ao analisar o arquivo. Verifique se o arquivo está no formato CSV correto.")
except Exception as e:
    # Outros erros
    print(f"Ocorreu um erro: {e}")