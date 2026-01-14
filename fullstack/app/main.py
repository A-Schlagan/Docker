from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, db_engine
import models
import crud
import schemas

models.Base.metadata.create_all(bind=db_engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Domain
    allow_credentials=True, # Anmeldeinformationen
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def root():
    return {"message": "Alex, Herzlich Willkommen!"}

@app.get("/kunden")
async def read_kunden(db: Session = Depends(get_db)):
    datensaetze = crud.get_Kunden(db)
    return datensaetze

@app.get("/kunden/{id}")
async def read_kunde(id, db: Session = Depends(get_db)):
    datensatz = crud.get_Kunde(db, id)
    return datensatz

@app.post("/kunden")
async def create_kunde(kunde: schemas.KundenCreate, db: Session = Depends(get_db)):
    datensatz = crud.create_Kunden(db, kunde)
    return datensatz

@app.delete("/kunden/{id}")
async def delete_kunden(id: int, db: Session = Depends(get_db)):
    erg = crud.delete_Kunde(db, id)
    return erg

@app.patch("/kunden/{id}")
async def update_kunde(id: int, kunde: schemas.KundenCreate, db: Session = Depends(get_db)):
    erg = crud.update_Kunde(db, kunde, id)
    return erg

