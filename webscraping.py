import requests


def baixar_arquivo(url, endereco):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            with open(endereco, 'wb') as arquivo:
                arquivo.write(resposta.content)
        else:
            resposta.raise_for_status()
    except Exception as error:
        print(f'Algo deu errado -> {error}')


if __name__ == '__main__':
    url = 'http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras' \
          '/tiss/Padrao_tiss/tiss3/Padr%C3%A3o_TISS_Componente_Organizacional_202103.pdf'

    baixar_arquivo(url, 'componente.pdf')
