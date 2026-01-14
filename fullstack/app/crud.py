'''
create, read, update, delete funktionen
'''
from sqlalchemy.orm import Session 

import models
import schemas

def get_Kunden(db: Session):
    return db.query(models.Kunden).order_by(models.Kunden.id.asc()).all()

def get_Kunde(db: Session, id: int):
    return db.query(models.Kunden).filter(models.Kunden.id == id).first()

def create_Kunden(db: Session, kunde: schemas.KundenCreate):
    kunde_abruf = db.query(models.Kunden).filter(models.Kunden.email == kunde.email).first()
    if kunde_abruf:
        return "Der Kunde existiert bereits!"
    db_kunde = models.Kunden(**kunde.model_dump())
    db.add(db_kunde)
    db.commit()
    db.refresh(db_kunde)
    return db_kunde

def delete_Kunde(db: Session, id: int):
    kunde_abruf = db.query(models.Kunden).filter(models.Kunden.id == id).first()
    if not kunde_abruf:
        return "Gibt´s nicht!"
    db.delete(kunde_abruf)
    db.commit()
    return str(id) + " ist gelöscht!"
    
def update_Kunde(db:Session, kunde: schemas.KundenCreate, id: int):
    db_kunde = db.query(models.Kunden).filter(models.Kunden.id == id)
    if not db_kunde.first():
        return "Kunde nicht gefunden"
    db_kunde.update(kunde.model_dump())
    db.commit()
    return str(id) + " ist geändert!"
