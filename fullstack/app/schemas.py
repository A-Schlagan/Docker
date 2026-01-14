'''
Datenmodell muss überprüft werden, pydantic
'''

from pydantic import BaseModel, Field

class KundeBase(BaseModel):
    geschlecht: str =Field('w' or 'm')
    firmenname: str = None
    vorname: str
    nachname: str = Field(max_length=50)
    email: str

class KundenCreate(KundeBase):
    pass





