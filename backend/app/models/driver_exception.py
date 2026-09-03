from datetime import time
from enum import Enum

from app.db.base import Base
from sqlalchemy import Enum as SQLEnum 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ExceptionStatus(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class DriverException(Base):
    __tablename__ = "driver_exceptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    driver_id: Mapped[int] = mapped_column(foreignkey=("drivers.id"), nullable=False)
    status: Mapped[ExceptionStatus] = mapped_column(SQLEnum(ExceptionStatus), nullable=False)
    exception_date: Mapped[date] = mapped_column(nullable=False)
    reason: Mapped[str | None] = mapped_column(nullable=True)
    driver = Mapped["Driver"] = relationship("Driver", back_populates="exceptions")
