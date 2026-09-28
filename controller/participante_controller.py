from fastapi import APIRouter, status
from typing import List
from model.participante import ParticipanteCreate, Participante, ParticipanteUpdate
from service.participante_service import ParticipanteService

router = APIRouter(prefix="/participantes", tags=["Participantes"])

@router.post("/", response_model=Participante, status_code=status.HTTP_201_CREATED)
def cadastrar_participante(participante_in: ParticipanteCreate):
    return ParticipanteService.cadastrar_participante(participante_in)

@router.get("/", response_model=List[Participante])
def listar_participantes():
    return ParticipanteService.listar_participantes()

@router.get("/{id}", response_model=Participante)
def consultar_participante(id: int):
    return ParticipanteService.consultar_participante(id)

@router.put("/{id}", response_model=Participante)
def atualizar_participante(id: int, participante_in: ParticipanteUpdate):
    return ParticipanteService.atualizar_participante(id, participante_in)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_participante(id: int):
    ParticipanteService.excluir_participante(id)
