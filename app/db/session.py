from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mssql+pyodbc://admin:admin#202@note-app.cvnhfnhhimdb.ap-northeast-1.rds.amazonaws.com:1433/todo?driver=ODBC+Driver+17+for+SQL+Server"

engin = create_engine(DATABASE_URL, echo=True, future=True)

session = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()
