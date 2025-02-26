from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Note(BaseModel):
    title: str
    content: str

notes = {}

@app.post("/notes")
def create_note(note: Note):
    note_id = str(uuid4())
    notes[note_id] = {"title": note.title, "content": note.content}
    return {"id": note_id, **notes[note_id]}

@app.get("/notes")
def get_notes():
    return [{"id": note_id, **data} for note_id, data in notes.items()]

@app.get("/notes/{note_id}")
def get_note(note_id: str):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Anotação não encontrada.")
    return {"id": note_id, **notes[note_id]}

@app.put("/notes/{note_id}")
def update_note(note_id: str, note: Note):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Anotação não encontrada.")
    notes[note_id] = {"title": note.title, "content": note.content}
    return {"id": note_id, **notes[note_id]}

@app.delete("/notes/{note_id}")
def delete_note(note_id: str):
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Anotação não encontrada.")
    del notes[note_id]
    return {"message": "Anotação excluída com sucesso."}