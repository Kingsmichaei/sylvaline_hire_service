from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(nullable=False)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)
    place_id: Mapped[str] = mapped_column(unique=True, nullable=False)
    pickup_bookings = relationship("Booking", foreign_keys="[Booking.pickup_location_id]", back_populates="pickup_location")
    destination_bookings = relationship("Booking", foreign_keys="[Booking.destination_location_id]", back_populates="destination_location")
    