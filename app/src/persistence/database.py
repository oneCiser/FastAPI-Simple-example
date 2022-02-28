import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_USER = os.environ.get("POSTGRES_USER")
DATABASE_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DATABASE_NAME = os.environ.get("POSTGRES_DB")
DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@db:5432/{DATABASE_NAME}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




