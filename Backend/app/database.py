from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from config import db_url


engine = create_async_engine(db_url, echo=True)


AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()