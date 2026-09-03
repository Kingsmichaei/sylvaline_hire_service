from datetime import datetime
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Receipt(Base):
    __tablename__ = "receipts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    receipt_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    payment_id: Mapped[int] = mapped_column(ForeignKey("payments.id"), unique=True, nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    issued_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)
    file_url: Mapped[str] = mapped_column(nullable=False)
    payment: Mapped["Payment"] = relationship("Payment", back_populates="receipt")