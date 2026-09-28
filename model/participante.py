from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ParticipanteBase(BaseModel):
    nome: str = Field(..., min_length=1, description="O nome do participante não pode ser vazio")
    email: EmailStr = Field(..., description="O e-mail deve possuir formato válido")
    curso: str

class ParticipanteCreate(ParticipanteBase):
    pass

class Participante(ParticipanteBase):
    id: int

class ParticipanteUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1)
    email: Optional[EmailStr] = None
    curso: Optional[str] = None
