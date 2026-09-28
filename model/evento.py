from pydantic import BaseModel, Field, constr
from datetime import date
from typing import Optional

class EventoBase(BaseModel):
    titulo: str = Field(..., min_length=1, description="O título do evento não pode ser vazio")
    descricao: str
    data: date
    horario: str
    local: str
    capacidade: int = Field(..., gt=0, description="A capacidade do evento deve ser maior que zero")
    categoria: str

class EventoCreate(EventoBase):
    pass

class Evento(EventoBase):
    id: int

class EventoUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1)
    descricao: Optional[str] = None
    data: Optional[date] = None
    horario: Optional[str] = None
    local: Optional[str] = None
    capacidade: Optional[int] = Field(None, gt=0)
    categoria: Optional[str] = None
