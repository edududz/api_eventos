from database.db import eventos, inscricoes
from model.evento import EventoCreate, Evento, EventoUpdate
from typing import List, Dict
from fastapi import HTTPException

class EventoService:
    @staticmethod
    def _gerar_id() -> int:
        if not eventos:
            return 1
        return max(e["id"] for e in eventos) + 1

    @staticmethod
    def listar_eventos() -> List[Evento]:
        return [Evento(**e) for e in eventos]

    @staticmethod
    def cadastrar_evento(evento_in: EventoCreate) -> Evento:
        novo_id = EventoService._gerar_id()
        evento_dict = evento_in.model_dump()
        evento_dict["id"] = novo_id
        eventos.append(evento_dict)
        return Evento(**evento_dict)

    @staticmethod
    def consultar_evento(id: int) -> Evento:
        for e in eventos:
            if e["id"] == id:
                return Evento(**e)
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    @staticmethod
    def atualizar_evento(id: int, evento_in: EventoUpdate) -> Evento:
        for i, e in enumerate(eventos):
            if e["id"] == id:
                dados_atualizar = evento_in.model_dump(exclude_unset=True)
                eventos[i].update(dados_atualizar)
                return Evento(**eventos[i])
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    @staticmethod
    def excluir_evento(id: int):
        for i, e in enumerate(eventos):
            if e["id"] == id:
                del eventos[i]
                # Remover inscrições associadas
                inscricoes[:] = [insc for insc in inscricoes if insc["evento_id"] != id]
                return
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    @staticmethod
    def verificar_vagas(evento_id: int) -> bool:
        evento = EventoService.consultar_evento(evento_id)
        inscricoes_evento = [i for i in inscricoes if i["evento_id"] == evento_id]
        return len(inscricoes_evento) < evento.capacidade
