from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


#TODO: Get this via a KMS
POSTGRES_URL = "postgresql://dxxugmbupuujmi:74154795ba071772f0a9a65504717e382fff6a281911d648336e42c367ed5c02@ec2-54-216-17-9.eu-west-1.compute.amazonaws.com:5432/d38upmk8bt5he9"


engine = create_async_engine(POSTGRES_URL.replace("postgresql://", "postgresql+asyncpg://"), pool_size=100, future=True)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)
