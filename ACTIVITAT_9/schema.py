from pydantic import BaseModel

class UserDefault(BaseModel):
    id: int
    name: str
    email: str