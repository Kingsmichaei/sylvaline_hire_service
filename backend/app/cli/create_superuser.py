from getpass import getpass
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.init_db import init_db
from app.models.user import User, UserRole
from app.core.security import hash_password
from pydantic import EmailStr, TypeAdapter, ValidationError

def create_superuser():
    init_db()
    db: Session = SessionLocal()

    try:
        while True:
            email_input = input("Email: ").strip()
            try:
                email = TypeAdapter(EmailStr).validate_python(email_input)
                break
            except ValidationError:
                print("Error: Please enter a valid email address.")

        while True:
            password = getpass("Password: ")
            
            if not password:
                print("Error: Password cannot be empty.")
                continue
        
            password_confirmation = getpass("Password (again): ")

            if password != password_confirmation:
                print("Error: Passwords do not match.")
                continue
            break

        existing_user = db.query(User).filter(
            User.email == email
        ).first()

        if existing_user:
            print("Error: A user with this email already exists.")
            return

        hashed_password = hash_password(password)

        user = User(
            email=email,
            password_hash=hashed_password,
            role=UserRole.SUPER_ADMIN,
            is_active=True
        )

        db.add(user)
        db.commit()

        print(f"Superuser {email} created successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error creating superuser: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    create_superuser()