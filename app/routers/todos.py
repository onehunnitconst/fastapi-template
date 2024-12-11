from fastapi import APIRouter
from app.services import todo_service as service
from app.models.todo import Todo
from app.models.engine import SessionDep

router = APIRouter(prefix="/todo")

@router.post("/")
def create_todo(todo: Todo, session: SessionDep):
  return service.create_todo(todo, session)

@router.get("/{id}")
def read_todo(id: int, session: SessionDep):
  return service.read_todo(id, session)