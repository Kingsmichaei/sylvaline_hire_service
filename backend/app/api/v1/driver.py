from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import require_role
from app.db.database import get_db
from app.core.security import hash_password
from app.models.user import User, UserRole
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverResponse

router = APIRouter(
    tags=["Drivers"]
)

@router.post("/", response_model=DriverResponse)
def create_driver(
    driver_data: DriverCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role(UserRole.SUPER_ADMIN))
):
    existing_user = db.query(User).filter(
        User.email == driver_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists"
        )

    try:
        password_hash = hash_password(driver_data.password)

        user = User(
            email=driver_data.email,
            password_hash=password_hash,
            role=UserRole.DRIVER,
            is_active=True
        )

        db.add(user)
        db.flush()

        driver = Driver(
            user_id=user.id,
            first_name=driver_data.first_name,
            last_name=driver_data.last_name,
            phone=driver_data.phone,
            address=driver_data.address,
            has_valid_license=driver_data.has_valid_license
        )

        db.add(driver)
        db.commit()

    except Exception:
        db.rollback()
        raise

    return {
        "id": driver.id,
        "email": driver.user.email,
        "first_name": driver.first_name,
        "last_name": driver.last_name,
        "phone": driver.phone,
        "address": driver.address,
        "has_valid_license": driver.has_valid_license,
        "status": driver.status.value
    }
