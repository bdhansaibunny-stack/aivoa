from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class HCPProfileBase(BaseModel):
    name: str
    specialty: Optional[str] = None
    title: Optional[str] = None
    organization: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None

class HCPProfileCreate(HCPProfileBase):
    pass

class HCPProfileUpdate(BaseModel):
    name: Optional[str] = None
    specialty: Optional[str] = None
    title: Optional[str] = None
    organization: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None

class HCPProfileResponse(HCPProfileBase):
    id: UUID
    interaction_count: int
    last_interaction: Optional[datetime] = None
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class HCPProfileListResponse(BaseModel):
    total: int
    items: list
