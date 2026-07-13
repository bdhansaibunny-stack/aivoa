from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.hcp import HCPProfileCreate, HCPProfileUpdate, HCPProfileResponse
from app.crud import hcp as crud
from uuid import UUID

router = APIRouter(prefix="/api/v1/hcps", tags=["hcps"])

@router.post("/", response_model=HCPProfileResponse, status_code=201)
def create_hcp(hcp: HCPProfileCreate, db: Session = Depends(get_db)):
    return crud.create_hcp(db, hcp)

@router.get("/{hcp_id}", response_model=HCPProfileResponse)
def get_hcp(hcp_id: UUID, db: Session = Depends(get_db)):
    hcp = crud.get_hcp(db, hcp_id)
    if not hcp:
        raise HTTPException(status_code=404, detail="HCP not found")
    return hcp

@router.put("/{hcp_id}", response_model=HCPProfileResponse)
def update_hcp(hcp_id: UUID, hcp: HCPProfileUpdate, db: Session = Depends(get_db)):
    db_hcp = crud.update_hcp(db, hcp_id, hcp)
    if not db_hcp:
        raise HTTPException(status_code=404, detail="HCP not found")
    return db_hcp

@router.delete("/{hcp_id}", status_code=204)
def delete_hcp(hcp_id: UUID, db: Session = Depends(get_db)):
    success = crud.delete_hcp(db, hcp_id)
    if not success:
        raise HTTPException(status_code=404, detail="HCP not found")
