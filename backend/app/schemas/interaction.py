from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any
from uuid import UUID

class InteractionBase(BaseModel):
    hcp_id: UUID
    hcp_name: str
    interaction_date: datetime
    interaction_type: Optional[str] = None
    summary: Optional[str] = None
    topics: Optional[str] = None
    outcomes: Optional[str] = None
    next_steps: Optional[str] = None
    raw_input: Optional[str] = None

class InteractionCreate(InteractionBase):
    pass

class InteractionUpdate(BaseModel):
    interaction_type: Optional[str] = None
    summary: Optional[str] = None
    topics: Optional[str] = None
    outcomes: Optional[str] = None
    next_steps: Optional[str] = None

class InteractionResponse(InteractionBase):
    id: UUID
    entities: Optional[Dict[str, Any]] = None
    created_by: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class InteractionListResponse(BaseModel):
    total: int
    items: list
