import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL")
REDIS_URL = os.getenv("REDIS_URL")


class Settings:
    SQL_USER: str = os.getenv("POSTGRES_USER")
    SQL_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    SQL_SERVER: str = os.getenv("POSTGRES_SERVER")
    SQL_PORT: str = os.getenv("POSTGRES_PORT")
    SQL_DATABASE: str = os.getenv("POSTGRES_DATABASE")
    DATABASE_URL = f"postgresql://{SQL_USER}:{SQL_PASSWORD}@{SQL_SERVER}:{SQL_PORT}/"

    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT: str = os.getenv('REDIS_PORT')
    REDIS_DATABASE: str = os.getenv('REDIS_DATABASE')

    REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'


settings = Settings()
