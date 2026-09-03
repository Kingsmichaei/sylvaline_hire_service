from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from enum import Enum
from sqlalchemy import Enum as SqlEnum
from datetime import datetime


class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"
    
class PaymentMethod(str, Enum):
    ONLINE = "online"
    CASH = "cash"
    POS = "pos"

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.id"), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(SqlEnum(PaymentStatus), default=PaymentStatus.PENDING, nullable=False)
    payment_method: Mapped[PaymentMethod] = mapped_column(SqlEnum(PaymentMethod), nullable=False)
    transaction_reference: Mapped[str | None] = mapped_column(unique=True, nullable=True)
    payment_reference: Mapped[str | None] = mapped_column(unique=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    booking: Mapped["Booking"] = relationship("Booking", back_populates="payment")
    receipt: Mapped["Receipt"] = relationship("Receipt", back_populates="payment", uselist=False)