from sqlalchemy import Column, String, DateTime, Integer, UUID, Text
from sqlalchemy.dialects.postgresql import JSON
from app.database import Base
from datetime import datetime
import uuid

class HCPProfile(Base):
    __tablename__ = "hcp_profiles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False, index=True)
    specialty = Column(String(100), nullable=True)
    title = Column(String(100), nullable=True)
    organization = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True, index=True)
    phone = Column(String(20), nullable=True)
    location = Column(String(255), nullable=True)
    contact_info = Column(JSON, nullable=True)
    interaction_count = Column(Integer, default=0)
    last_interaction = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
