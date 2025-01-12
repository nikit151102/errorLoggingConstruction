from pydantic import BaseModel

class UserActionDto(BaseModel):
    user_id: str
    user_full_name: str
    email: str
    action: str