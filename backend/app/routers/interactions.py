from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.interaction import InteractionCreate, InteractionUpdate, InteractionResponse
from app.crud import interaction as crud
from uuid import UUID

router = APIRouter(prefix="/api/v1/interactions", tags=["interactions"])

@router.post("/", response_model=InteractionResponse, status_code=201)
def create_interaction(interaction: InteractionCreate, db: Session = Depends(get_db)):
    return crud.create_interaction(db, interaction)

@router.get("/{interaction_id}", response_model=InteractionResponse)
def get_interaction(interaction_id: UUID, db: Session = Depends(get_db)):
    interaction = crud.get_interaction(db, interaction_id)
    if not interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return interaction

@router.put("/{interaction_id}", response_model=InteractionResponse)
def update_interaction(interaction_id: UUID, interaction: InteractionUpdate, db: Session = Depends(get_db)):
    db_interaction = crud.update_interaction(db, interaction_id, interaction)
    if not db_interaction:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return db_interaction

@router.delete("/{interaction_id}", status_code=204)
def delete_interaction(interaction_id: UUID, db: Session = Depends(get_db)):
    success = crud.delete_interaction(db, interaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Interaction not found")
