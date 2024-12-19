import requests


def extract_dados_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    headers = {
        "Accept": "application/json",
        "User-Agent": "MinhaAplicacao/1.0"
    }

    # Moeda de consulta
    params = {"currency": "USD"}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data


def transform_dados_bitcoin(data):    
    valor =  data["data"]["amount"]
    criptomoeda = data["data"]["base"]
    moeda = data["data"]["currency"]

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda
    }
    return dados_transformados 

if __name__ == "__main__":
    dados = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados)
    print(dados_transformados)