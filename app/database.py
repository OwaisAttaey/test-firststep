from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a Session class for the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a function to get the database engine
def get_engine():
    return engine

# Define a function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
