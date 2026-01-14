'''
Datenbank Tabellen angelegt und definiert
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

# database.py
from database import Base

class Kunden(Base):
    __tablename__ ="Kunden"
    id = Column(Integer, primary_key=True, index=True)
    geschlecht = Column(Enum('w','m'), nullable=True)
    firmenname = Column(String(20))
    vorname = Column(String(30))
    nachname = Column(String(40))
    email = Column(String(30), nullable=False, unique=True, index=True)