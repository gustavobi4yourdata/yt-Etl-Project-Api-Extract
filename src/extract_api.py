import requests
import time
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

from database import Base, BitcoinPreco


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Cria a conexão com o banco de dados
POSTGRES_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Cria a engine e a sessão
engine = create_engine(POSTGRES_DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso!")


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
    timestamp = datetime.now()

    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }

    return dados_transformados

def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no postgreSQL !")


if __name__ == "__main__":
    criar_tabela()
    print("Iniciando ETL com atualização a cada 15 segundos...")

    while True:
        try:
            dados_json = extract_dados_bitcoin()
            if  dados_json:
                dados_tratados = transform_dados_bitcoin(dados_json)
                print("Dados Tratados:", dados_tratados)
                salvar_dados_postgres(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interropido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)

