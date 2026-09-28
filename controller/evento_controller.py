from fastapi import APIRouter, status
from typing import List
from model.evento import EventoCreate, Evento, EventoUpdate
from service.evento_service import EventoService
from service.participante_service import ParticipanteService
from model.participante import Participante

router = APIRouter(prefix="/eventos", tags=["Eventos"])

@router.post("/", response_model=Evento, status_code=status.HTTP_201_CREATED)
def cadastrar_evento(evento_in: EventoCreate):
    return EventoService.cadastrar_evento(evento_in)

@router.get("/", response_model=List[Evento])
def listar_eventos():
    return EventoService.listar_eventos()

@router.get("/{id}", response_model=Evento)
def consultar_evento(id: int):
    return EventoService.consultar_evento(id)

@router.put("/{id}", response_model=Evento)
def atualizar_evento(id: int, evento_in: EventoUpdate):
    return EventoService.atualizar_evento(id, evento_in)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_evento(id: int):
    EventoService.excluir_evento(id)

@router.post("/{evento_id}/inscricoes/{participante_id}", status_code=status.HTTP_201_CREATED)
def inscrever_participante(evento_id: int, participante_id: int):
    return ParticipanteService.inscrever_em_evento(evento_id, participante_id)

@router.get("/{evento_id}/inscricoes", response_model=List[Participante])
def consultar_inscritos(evento_id: int):
    return ParticipanteService.listar_inscritos_evento(evento_id)
