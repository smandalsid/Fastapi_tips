from enum import Enum
from pydantic import AnyUrl, BaseModel, EmailStr, Field
from typing import Optional

class VersionType(Enum):
    ORIGINAL = 'O'
    BASELINE = 'B'

class TestBase(BaseModel):
    first_name: str = Field(min_length=2, max_length=100)
    username: str = Field(min_length=1, max_length=123)
    email: EmailStr
    age: int = Field(ge=18, default=None)
    version_type: Optional[VersionType] = None

