from datetime import datetime
from enum import Enum
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class UserRole(str, Enum):
    SUPER_ADMIN = "super_admin"
    DRIVER = "driver"

class User(Base):
    __tablename__= "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(SqlEnum(UserRole), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)
    driver: Mapped["Driver | None"] = relationship("Driver", back_populates="user", uselist=False)