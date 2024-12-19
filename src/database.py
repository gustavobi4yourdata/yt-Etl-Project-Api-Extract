from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String , Integer, DateTime
from datetime import datetime


# Cria a classe Base do SQLAlchemy (Versão 2.x)
Base = declarative_base()

class  BitcoinPreco(Base):
    "Definindo a tabela no banco de dados"
    __tablename__ = "bitcoin_precos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)
    moeda = Column(String(50), nullable=False)
    data = Column(DateTime, default=datetime.now)
    timestamp = Column(DateTime, default=datetime.now)