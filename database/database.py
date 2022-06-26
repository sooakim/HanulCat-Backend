from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import environment

sqlalchemy_database_url = "postgresql://" + environment.db_user_name + ":" + environment.db_user_password + "@" + environment.db_host + ":" + environment.db_port + "/hanul_cat"
engine = create_engine(sqlalchemy_database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()