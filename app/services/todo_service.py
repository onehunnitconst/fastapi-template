from fastapi import HTTPException
from app.models.todo import Todo
from app.models.engine import SessionDep

def create_todo(todo: Todo, session: SessionDep) -> Todo:
  session.add(todo)
  session.commit()
  session.refresh(todo)
  return todo

def read_todo(id: int, session: SessionDep) -> Todo:
  todo = session.get(Todo, id)
  if not todo:
    raise HTTPException(status_code=404, detail="Todo not found")
  return todo