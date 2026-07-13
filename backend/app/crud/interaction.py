from sqlalchemy.orm import Session
from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate, InteractionUpdate
from uuid import UUID
from datetime import datetime
from typing import List, Optional

def create_interaction(db: Session, interaction: InteractionCreate) -> Interaction:
    db_interaction = Interaction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

def get_interaction(db: Session, interaction_id: UUID) -> Optional[Interaction]:
    return db.query(Interaction).filter(Interaction.id == interaction_id).first()

def get_interactions_by_hcp(db: Session, hcp_id: UUID, skip: int = 0, limit: int = 100) -> List[Interaction]:
    return db.query(Interaction).filter(Interaction.hcp_id == hcp_id).offset(skip).limit(limit).all()

def get_all_interactions(db: Session, skip: int = 0, limit: int = 100) -> List[Interaction]:
    return db.query(Interaction).offset(skip).limit(limit).all()

def update_interaction(db: Session, interaction_id: UUID, interaction: InteractionUpdate) -> Optional[Interaction]:
    db_interaction = get_interaction(db, interaction_id)
    if db_interaction:
        update_data = interaction.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_interaction, field, value)
        db_interaction.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_interaction)
    return db_interaction

def delete_interaction(db: Session, interaction_id: UUID) -> bool:
    db_interaction = get_interaction(db, interaction_id)
    if db_interaction:
        db.delete(db_interaction)
        db.commit()
        return True
    return False

def get_interactions_count(db: Session, hcp_id: Optional[UUID] = None) -> int:
    query = db.query(Interaction)
    if hcp_id:
        query = query.filter(Interaction.hcp_id == hcp_id)
    return query.count()
