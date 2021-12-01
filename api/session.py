from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

#TODO: Get this via a KMS
POSTGRES_URL = "postgres://aitkyjrlwvciaq:ca20df7506e91601e3233796eecd9e61335b76095428aaeae2c54d271e026dbb@ec2-54-228-139-34.eu-west-1.compute.amazonaws.com:5432/dc3790mkg38clg"


engine = create_async_engine(POSTGRES_URL.replace("postgresql://", "postgresql+asyncpg://"), pool_size=100, future=True)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)
