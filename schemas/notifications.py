from pydantic import BaseModel

class UserActionDto(BaseModel):
    user_id: str
    user_full_name: str
    action: str