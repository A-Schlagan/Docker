'''
Docstring for database
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Parameter für den Connect
DATABASE_URL ="mysql+mysqldb://root:DAA@database:3306/adressen"
#Motor
db_engine = create_engine(DATABASE_URL)
#Session
SessionLocal = sessionmaker(bind=db_engine)
#Tabellenobjekte
Base = declarative_base()
