import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import settings

DATABASE_URL = "postgresql://postgres:postgres@172.17.0.1:5432/postgres"

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    sqlalchemy.MetaData.create_all(engine)


# async def async_main():
#     engine = create_async_engine(
#         "postgresql+asyncpg://postgres:postgres@postgres:5432/", echo=True,
#     )
#
#     async with engine.connect() as conn:
#         result = await conn.execute(sa.text('select email from users'))
#         print(result.fetchall())
#     await engine.dispose()
#
#
# asyncio.run(async_main())
#
#
# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)
#
#
# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(
#         engine, class_=AsyncSession, expire_on_commit=False
#     )
#     async with async_session() as session:
#         yield session

