from pydantic import BaseModel

class ErrorResponseDto(BaseModel):
    httpStatus: int
    details: str
    timestamp: str

class FrontendErrorLogDto(BaseModel):
    errorMessage: str
    details: str
    url: str
    username: str
    timestamp: str
