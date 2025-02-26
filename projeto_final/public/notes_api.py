# Importando as bibliotecas necessárias do FastAPI e outras
from fastapi import FastAPI, HTTPException  # FastAPI para criar a API e HTTPException para tratar erros
from fastapi.staticfiles import StaticFiles  # Para servir arquivos estáticos, como o HTML
from fastapi.responses import FileResponse  # Para retornar o arquivo HTML quando acessamos a raiz
from pydantic import BaseModel  # BaseModel para validar os dados da anotação

# Criando a aplicação FastAPI
app = FastAPI()

# Definindo como vai ser a estrutura dos dados de uma anotação
class Note(BaseModel):
    title: str  # Título da anotação
    content: str  # Conteúdo da anotação

# Dicionário para armazenar as anotações em memória
notes = {}

# Contador para gerar os IDs das anotações
id_counter = 1

# Rota para servir o arquivo index.html quando a página principal for acessada
@app.get("/")
def read_root():
    return FileResponse("index.html")  # Retorna o arquivo HTML na página inicial

# Rota para criar uma nova anotação
@app.post("/notes")
def create_note(note: Note):
    global id_counter
    note_id = f"{id_counter:05d}"  # Gera o ID com 5 dígitos, com zeros à esquerda, ex: 00001
    notes[note_id] = {"title": note.title, "content": note.content}  # Armazenar a anotação no dicionário
    id_counter += 1  # Incrementa o contador para o próximo ID
    return {"id": note_id, **notes[note_id]}  # Retorna o ID e os dados da anotação criada

# Rota para listar todas as anotações
@app.get("/notes")
def get_notes():
    return [{"id": note_id, **data} for note_id, data in notes.items()]  # Retorna todas as anotações armazenadas

# Rota para obter uma anotação específica, usando o ID dela
@app.get("/notes/{note_id}")
def get_note(note_id: str):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Anotação não encontrada.")  # Retorna erro se a anotação não existir
    return {"id": note_id, **notes[note_id]}  # Retorna a anotação encontrada

# Rota para atualizar uma anotação existente
@app.put("/notes/{note_id}")
def update_note(note_id: str, note: Note):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Anotação não encontrada.")  # Retorna erro se a anotação não existir
    notes[note_id] = {"title": note.title, "content": note.content}  # Atualiza os dados da anotação
    return {"id": note_id, **notes[note_id]}  # Retorna a anotação atualizada

# Rota para excluir uma anotação
@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Anotação não encontrada.")  # Retorna erro se a anotação não existir
    del notes[note_id]  # Exclui a anotação do dicionário
    return {"message": "Anotação excluída com sucesso"}  # Retorna uma mensagem confirmando a exclusão