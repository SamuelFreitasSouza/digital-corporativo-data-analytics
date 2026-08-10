import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


def testar_conexao():
    try:
        with engine.connect() as connection:
            resultado = connection.execute(text("SELECT 1"))
            print("Conexão realizada com sucesso!")
            print(resultado.fetchone())

    except Exception as erro:
        print("Erro ao conectar ao banco:")
        print(erro)


if __name__ == "__main__":
    testar_conexao()