from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from controller.evento_controller import router as evento_router
from controller.participante_controller import router as participante_router

app = FastAPI(
    title="API de Gerenciamento de Eventos Acadêmicos",
    description="API RESTful para gerenciar eventos e participantes desenvolvida em FastAPI.",
    version="1.0.0"
)

app.include_router(evento_router)
app.include_router(participante_router)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
