import uuid
from datetime import datetime

from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.domain.models.events import Event
from src.core.domain.session import Base


class File(Base):
    __tablename__ = 'files'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    alias: Mapped[uuid.UUID] = mapped_column(String(36), default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    extension: Mapped[str] = mapped_column(String(10))
    event_id: Mapped[str] = mapped_column(String(36), ForeignKey("events.id", ondelete="CASCADE"))

    event: Mapped["Event"] =  relationship(back_populates='files')



