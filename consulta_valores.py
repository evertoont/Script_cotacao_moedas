import requests
import pandas
import decimal


def converter_data(data):
    dia = data[8:]+'/'+data[5:7]+'/'+data[0:4]
    return dia


def chave_de_acesso(chave='c45326ac410e55c9568091de9161ca9e'):
    url = f'http://data.fixer.io/api/latest?access_key={chave}'
    return url


def converter_em_reais(valor_reais, valor_estrangeiro):
    conversao = round(valor_reais / valor_estrangeiro, 2)
    return conversao


def exportar_tabela(lista_moedas, lista_valores, data):
    celulas = pandas.DataFrame(
        {'Moedas': lista_moedas, 'Valores': lista_valores, 'Ultimo acesso': data})
    celulas.to_csv('Cotação das moedas.csv', index=False, sep=';', decimal=',')
    print("Tabela exportada com sucesso!")


def main():
    print("Acessando base de dados...")
    resposta = requests.get(chave_de_acesso())
    if resposta.status_code == 200:
        print("Conexão com a base de dados estabelecida com sucesso...")

        dados = resposta.json()
        data = converter_data(dados['date'])
        cotacao_USD = converter_em_reais(
            dados['rates']['BRL'], dados['rates']['USD'])
        coracao_GBP = converter_em_reais(
            dados['rates']['BRL'], dados['rates']['GBP'])
        cotacao_EUR = converter_em_reais(
            dados['rates']['BRL'], dados['rates']['EUR'])
        cotacao_JPY = converter_em_reais(
            dados['rates']['BRL'], dados['rates']['JPY'])
        cotacao_BTC = converter_em_reais(
            dados['rates']['BRL'], dados['rates']['BTC'])

        print("--------------------------------------------------")
        print(f'Última atualização: {data}')
        print("------------------------------")
        print(f'Dollar: R$ {cotacao_USD}')
        print(f'Libra Esterlina: R$ {coracao_GBP}')
        print(f'Euro: R$ {cotacao_EUR}')
        print(f'Ien Japonês: R$ {cotacao_JPY}')
        print(f'Bitcoin: R$ {cotacao_BTC}')
        print("--------------------------------------------------")

        exportar_tabela(['Dollar ', 'Libra Esterlina', 'Euro', 'Ien Japones', 'Bitcoin'],
                        [cotacao_USD, coracao_GBP, cotacao_EUR, cotacao_JPY, cotacao_BTC], data)

    else:
        print("Erro ao acessar a base de dados")


if __name__ == '__main__':
    main()

