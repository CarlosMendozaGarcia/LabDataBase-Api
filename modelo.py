from pydantic import BaseModel
from typing import Optional

class DataContinente(BaseModel):
    _id: str
    casos_totales: int
    nro_muertes_totales: int
    continente: Optional[str]= None

class DataSurAmerica(BaseModel):
    _id: str
    casos_totales: int
    nro_muertes_totales: int
    pais: Optional[str]= None