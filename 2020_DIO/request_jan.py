import requests  #executar antes: pip install requests ou py -m pip install -U requests

def retorna_dados_cep(cep):
    print("\n* CEP - NÃO ENCONTRADO *")
    response = requests.get('https://viacep.com.br/ws/01001000/jsonNNNN/') #retorna 400 = não encontrado
    print(response.status_code)
    print(response.text)
    #print(response.json())

    print("\n* CEP - ENCONTRADO *")
    response = requests.get('https://viacep.com.br/ws/01001000/json/') #retorna 200 = encontrado
    print(response.status_code)
    print("\n--> TEXT")
    print(response.text)
    print("\n--> JSON")
    print(response.json())

    print("\n* JSON LOGRADOURO *")
    dados_cep = response.json()
    print(dados_cep['logradouro'])

    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


if __name__ == '__main__':     #garante que será executado somente se chamado pelo próprio arquivo

    print("\n*** TESTE 1: CHAMA API CEP ***")
    retorna_dados_cep('22041001')

    print("\n*** TESTE 2: CHAMA API POKEMON - SOLICITA DADOS PIKACHU ***")
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print("\n* REQUEST ITEM ESPECÍFICO PIKACHU *")
    print("\n --> MOVE ")
    print(dados_pokemon['moves'][2])
    print("\n --> FORMA ")
    print(dados_pokemon['sprites']['front_shiny'])

