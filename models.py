from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
