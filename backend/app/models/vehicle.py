from enum import Enum
from sqlalchemy import Enum as SQLEnum
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class VehicleStatus(str, Enum):
    AVAILABLE = "available"  # The vehicle is AVAILABLE for use
    INACTIVE = "inactive" # The vehicle is not AVAILABLE for use
    MAINTENANCE = "maintenance" # The vehicle is not AVAILABLE for use due to maintenance
    BOOKED = "booked" # The vehicle is BOOKED for use

class VehicleType(str, Enum):
    PASSENGER = "passenger"  # The vehicle is a passenger vehicle
    LOAD = "load"  # The vehicle is a load vehicle
    BOTH = "both"  # The vehicle can be used for both passenger and load
    
class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    make: Mapped[str] = mapped_column(nullable=False)
    model: Mapped[str] = mapped_column(nullable=False)
    color: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[VehicleStatus] = mapped_column(SQLEnum(VehicleStatus), default=VehicleStatus.AVAILABLE, nullable=False)
    registration_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    license_plate: Mapped[str] = mapped_column(unique=True, nullable=False)
    seating_capacity: Mapped[int] = mapped_column(nullable=False)
    vehicle_type: Mapped[VehicleType] = mapped_column(SQLEnum(VehicleType), nullable=False)   
    bookings: Mapped[list["Booking"]] = relationship("Booking", back_populates="vehicle")