from pydantic import BaseModel, EmailStr

class DriverCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: str
    address: str
    has_valid_license: bool = False  


class DriverResponse(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    phone: str
    address: str
    has_valid_license: bool
    status: str
