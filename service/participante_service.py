from database.db import participantes, inscricoes
from model.participante import ParticipanteCreate, Participante, ParticipanteUpdate
from service.evento_service import EventoService
from typing import List
from fastapi import HTTPException

class ParticipanteService:
    @staticmethod
    def _gerar_id() -> int:
        if not participantes:
            return 1
        return max(p["id"] for p in participantes) + 1

    @staticmethod
    def listar_participantes() -> List[Participante]:
        return [Participante(**p) for p in participantes]

    @staticmethod
    def cadastrar_participante(participante_in: ParticipanteCreate) -> Participante:
        novo_id = ParticipanteService._gerar_id()
        participante_dict = participante_in.model_dump()
        participante_dict["id"] = novo_id
        participantes.append(participante_dict)
        return Participante(**participante_dict)

    @staticmethod
    def consultar_participante(id: int) -> Participante:
        for p in participantes:
            if p["id"] == id:
                return Participante(**p)
        raise HTTPException(status_code=404, detail="Participante não encontrado.")

    @staticmethod
    def atualizar_participante(id: int, participante_in: ParticipanteUpdate) -> Participante:
        for i, p in enumerate(participantes):
            if p["id"] == id:
                dados_atualizar = participante_in.model_dump(exclude_unset=True)
                participantes[i].update(dados_atualizar)
                return Participante(**participantes[i])
        raise HTTPException(status_code=404, detail="Participante não encontrado.")

    @staticmethod
    def excluir_participante(id: int):
        for i, p in enumerate(participantes):
            if p["id"] == id:
                del participantes[i]
                # Remover inscrições associadas
                inscricoes[:] = [insc for insc in inscricoes if insc["participante_id"] != id]
                return
        raise HTTPException(status_code=404, detail="Participante não encontrado.")

    @staticmethod
    def inscrever_em_evento(evento_id: int, participante_id: int):
        # 1. Verificar se o evento existe
        EventoService.consultar_evento(evento_id)
        
        # 2. Verificar se o participante existe
        ParticipanteService.consultar_participante(participante_id)

        # 3. Verificar se o participante já está inscrito
        for insc in inscricoes:
            if insc["evento_id"] == evento_id and insc["participante_id"] == participante_id:
                raise HTTPException(status_code=400, detail="Participante já está inscrito neste evento.")

        # 4. Verificar se o evento ainda possui vagas
        if not EventoService.verificar_vagas(evento_id):
            raise HTTPException(status_code=400, detail="Não existem vagas disponíveis para este evento.")

        inscricoes.append({"evento_id": evento_id, "participante_id": participante_id})
        return {"detail": "Inscrição realizada com sucesso."}

    @staticmethod
    def listar_inscritos_evento(evento_id: int) -> List[Participante]:
        # Verificar se o evento existe
        EventoService.consultar_evento(evento_id)

        participantes_ids = [insc["participante_id"] for insc in inscricoes if insc["evento_id"] == evento_id]
        inscritos = [Participante(**p) for p in participantes if p["id"] in participantes_ids]
        return inscritos
