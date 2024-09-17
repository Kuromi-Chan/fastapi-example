from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.domain.session import Base


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    files: Mapped[list["File"]] = relationship(back_populates='event')

