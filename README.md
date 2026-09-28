# API de Gerenciamento de Eventos Acadêmicos

Esta é uma API RESTful para gerenciar eventos acadêmicos, participantes e inscrições, desenvolvida em Python utilizando FastAPI.

## Funcionalidades

- **Gerenciamento de Eventos**: Cadastro, consulta, listagem, atualização e exclusão de eventos.
- **Gerenciamento de Participantes**: Cadastro, consulta, listagem, atualização e exclusão de participantes.
- **Inscrições**: Inscrição de participantes em eventos e consulta de inscritos por evento.
- **Validação de Dados**: Validação robusta de entradas com Pydantic, garantindo dados íntegros.
- **Tratamento de Erros**: Respostas HTTP apropriadas e detalhadas para falhas.

## Pré-requisitos

- Python 3.8+
- O pacote `pip` (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório ou baixe o projeto.
2. Navegue até a pasta do projeto:
   ```bash
   cd api_eventos
   ```
3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Para iniciar o servidor de desenvolvimento, execute:

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## Documentação e Testes

Ao rodar a API, você pode acessar a documentação interativa baseada no Swagger UI. Ela permite testar todas as rotas diretamente do navegador.

Acesse:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Principais Rotas

### Eventos
- `GET /eventos` - Lista todos os eventos
- `POST /eventos` - Cadastra um novo evento
- `GET /eventos/{id}` - Consulta um evento pelo ID
- `PUT /eventos/{id}` - Atualiza um evento
- `DELETE /eventos/{id}` - Exclui um evento
- `POST /eventos/{evento_id}/inscricoes/{participante_id}` - Inscreve um participante no evento
- `GET /eventos/{evento_id}/inscricoes` - Lista os participantes inscritos no evento

### Participantes
- `GET /participantes` - Lista todos os participantes
- `POST /participantes` - Cadastra um novo participante
- `GET /participantes/{id}` - Consulta um participante pelo ID
- `PUT /participantes/{id}` - Atualiza um participante
- `DELETE /participantes/{id}` - Exclui um participante

## Estrutura do Projeto (MVC)

O projeto está organizado visando a separação de responsabilidades (MVC):

- `main.py`: Ponto de entrada da aplicação FastAPI.
- `controller/`: Contém as rotas e validações de entrada HTTP.
- `model/`: Define os modelos de dados utilizando Pydantic para validação.
- `service/`: Contém as regras de negócio e manipulação dos dados.
- `database/`: Simulação de um banco de dados utilizando estruturas em memória.
