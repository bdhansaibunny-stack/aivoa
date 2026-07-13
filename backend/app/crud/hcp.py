from sqlalchemy.orm import Session
from app.models.hcp import HCPProfile
from app.schemas.hcp import HCPProfileCreate, HCPProfileUpdate
from uuid import UUID
from datetime import datetime
from typing import List, Optional

def create_hcp(db: Session, hcp: HCPProfileCreate) -> HCPProfile:
    db_hcp = HCPProfile(**hcp.dict())
    db.add(db_hcp)
    db.commit()
    db.refresh(db_hcp)
    return db_hcp

def get_hcp(db: Session, hcp_id: UUID) -> Optional[HCPProfile]:
    return db.query(HCPProfile).filter(HCPProfile.id == hcp_id).first()

def get_hcp_by_name(db: Session, name: str) -> Optional[HCPProfile]:
    return db.query(HCPProfile).filter(HCPProfile.name.ilike(f"%{name}%")).first()

def get_all_hcps(db: Session, skip: int = 0, limit: int = 100) -> List[HCPProfile]:
    return db.query(HCPProfile).offset(skip).limit(limit).all()

def update_hcp(db: Session, hcp_id: UUID, hcp: HCPProfileUpdate) -> Optional[HCPProfile]:
    db_hcp = get_hcp(db, hcp_id)
    if db_hcp:
        update_data = hcp.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_hcp, field, value)
        db_hcp.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_hcp)
    return db_hcp

def delete_hcp(db: Session, hcp_id: UUID) -> bool:
    db_hcp = get_hcp(db, hcp_id)
    if db_hcp:
        db.delete(db_hcp)
        db.commit()
        return True
    return False

def get_hcps_count(db: Session) -> int:
    return db.query(HCPProfile).count()

def update_hcp_interaction_count(db: Session, hcp_id: UUID) -> Optional[HCPProfile]:
    db_hcp = get_hcp(db, hcp_id)
    if db_hcp:
        db_hcp.interaction_count += 1
        db_hcp.last_interaction = datetime.utcnow()
        db.commit()
        db.refresh(db_hcp)
    return db_hcp
