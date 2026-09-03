from datetime import time, date, datetime
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from enum import Enum
from sqlalchemy import Enum as SqlEnum

class ServiceType(str, Enum):
    PASSENGER = "passenger"
    LOAD = "load"

class BookingStatus(str, Enum):
    PENDING = "pending"
    AWAITING_DRIVER = "awaiting_driver"
    AWAITING_PAYMENT = "awaiting_payment"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    CANCELED = "canceled"
    COMPLETED = "completed"
    DRIVER_DECLINED = "driver_declined"
    EXPIRED = "expired"

class DriverOption(str, Enum):
    SELF_DRIVE = "self_drive"
    DRIVER_PROVIDED = "driver_provided"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"
    
class PaymentMethod(str, Enum):
    ONLINE = "online"
    CASH = "cash"
    POS = "pos"
    
class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    booking_reference: Mapped[str] = mapped_column(unique=True, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)
    service_type: Mapped[ServiceType] = mapped_column(SqlEnum(ServiceType), nullable=False)
    purpose: Mapped[str] = mapped_column(nullable=False)
    driver_option: Mapped[DriverOption] = mapped_column(SqlEnum(DriverOption), nullable=False)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.id"), nullable=False)
    driver_id: Mapped[int | None] = mapped_column(ForeignKey("drivers.id"), nullable=True)
    status: Mapped[BookingStatus] = mapped_column(SqlEnum(BookingStatus), default=BookingStatus.PENDING, nullable=False)
    booking_date: Mapped[date] = mapped_column(nullable=False)
    start_date: Mapped[date] = mapped_column(nullable=False)
    end_date: Mapped[date] = mapped_column(nullable=False)
    pickup_location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"), nullable=False)
    destination_location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"), nullable=False)
    distance_km: Mapped[float | None] = mapped_column(nullable=True)
    estimated_duration: Mapped[time | None] = mapped_column(nullable=True)
    number_of_trips: Mapped[int] = mapped_column(default=1, nullable=False)
    load_description: Mapped[str | None] = mapped_column(nullable=True)
    base_price: Mapped[float] = mapped_column(nullable=False)
    driver_fee: Mapped[float] = mapped_column(nullable=False)
    additional_charges: Mapped[float] = mapped_column(nullable=False)
    discount: Mapped[float] = mapped_column(nullable=False)
    payment_status: Mapped[PaymentStatus] = mapped_column(SqlEnum(PaymentStatus), default=PaymentStatus.PENDING, nullable=False)
    payment_method: Mapped[PaymentMethod] = mapped_column(SqlEnum(PaymentMethod), nullable=False)
    total_amount: Mapped[float] = mapped_column(nullable=False)
    customer: Mapped["Customer"] = relationship("Customer", back_populates="bookings")
    vehicle: Mapped["Vehicle"] = relationship("Vehicle", back_populates="bookings")
    driver: Mapped["Driver | None"] = relationship("Driver", back_populates="bookings")
    pickup_location: Mapped["Location"] = relationship("Location", foreign_keys=[pickup_location_id], back_populates="pickup_bookings")
    destination_location: Mapped["Location"] = relationship("Location", foreign_keys=[destination_location_id], back_populates="destination_bookings")
    payment: Mapped["Payment | None"] = relationship("Payment", back_populates="booking", uselist=False)
    load_description: Mapped[str | None] = mapped_column(nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(nullable=True)
    cancellation_reason: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    customer_notes: Mapped[str | None] = mapped_column(nullable=True)
    admin_notes: Mapped[str | None] = mapped_column(nullable=True)