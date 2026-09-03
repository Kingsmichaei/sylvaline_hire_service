from enum import Enum
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


class DriverStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class Driver(Base):
    __tablename__ = "drivers"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(nullable=False)
    lastname: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    valid_driver_license: Mapped[bool] = mapped_column(default=False, nullable=False)
    status: Mapped[DriverStatus] = mapped_column(SqlEnum(DriverStatus), default=DriverStatus.ACTIVE, nullable=False)
    bookings: Mapped[list["Booking"]] = relationship("Booking", back_populates="driver")
    availabilities: Mapped[list["DriverAvailability"]] = relationship("DriverAvailability", back_populates="driver", cascade="all, delete-orphan")
    exceptions: Mapped[list["DriverException"]] = relationship("DriverException", back_populates="driver", cascade="all, delete-orphan")
    user: Mapped["User"] = relationship("User", back_populates="driver")