import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DATABASE: str = os.getenv("POSTGRES_DATABASE")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_DATABASE}:{POSTGRES_PORT}/postgres"

    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PORT: str = os.getenv('REDIS_PORT')
    REDIS_DATABASE: str = os.getenv('REDIS_DATABASE')
    REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'


settings = Settings()
