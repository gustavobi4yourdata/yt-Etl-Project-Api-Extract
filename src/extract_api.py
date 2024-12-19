import requests
import csv
import os


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

def load_dados_bitcoin(dados_transformados):
    os.makedirs("data", exist_ok=True)
    csv_path = "data/dados_bitcoin.csv"

    with open(csv_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dados_transformados.keys())
        writer.writerow(dados_transformados.values())


if __name__ == "__main__":
    dados = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados)
    salvar_dados = load_dados_bitcoin(dados_transformados)