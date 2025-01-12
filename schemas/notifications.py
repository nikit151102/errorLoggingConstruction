from pydantic import BaseModel

class UserActionDto(BaseModel):
    user_id: int
    user_full_name: str
    action: str