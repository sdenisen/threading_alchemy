import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print(os.environ.get("DB_CONNECTION"))
engine = create_engine(os.environ.get("DB_CONNECTION"))
SessionLocal = sessionmaker(bind=engine)
