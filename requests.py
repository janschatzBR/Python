import requests  #executar antes: pip install requests ou py -m pip install -U requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/01001000/json/') #retorna 200 = encontrado
    print(response.status_code)
    print(response.text)

    response = requests.get('https://viacep.com.br/ws/01001000/jsonn/') #retorna 400 = não encontrado
    print(response.status_code)
    print(response.text)
    print(response.json())

    dados_cep = response.json()
    print(dados_cep['logradouro']

    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


if __name__ == '__main__':     #garante que será executado somente se chamado pelo próprio arquivo

    retorna_dados_cep('22041001')

    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon['sprites']['front_shiny'])

