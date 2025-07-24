from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker

DATABASE_URL = "postgresql://postgres:080803@localhost/cloud_optimizer"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()