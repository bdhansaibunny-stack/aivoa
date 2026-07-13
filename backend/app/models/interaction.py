from sqlalchemy import Column, String, DateTime, Text, Integer, UUID
from sqlalchemy.dialects.postgresql import JSON
from app.database import Base
from datetime import datetime
import uuid

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    hcp_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    hcp_name = Column(String(255), nullable=False)
    interaction_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    interaction_type = Column(String(50), nullable=True)
    summary = Column(Text, nullable=True)
    topics = Column(String(500), nullable=True)
    outcomes = Column(Text, nullable=True)
    next_steps = Column(Text, nullable=True)
    entities = Column(JSON, nullable=True)
    raw_input = Column(Text, nullable=True)
    created_by = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
