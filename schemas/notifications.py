from pydantic import BaseModel

class NewUserNotificationDto(BaseModel):
    username: str

class NewJobNotificationDto(BaseModel):
    id: str
    title: str

class NewResumeNotificationDto(BaseModel):
    id: str
    username: str
