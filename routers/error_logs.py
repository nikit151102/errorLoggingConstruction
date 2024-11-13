from fastapi import APIRouter
from schemas.error_logs import ErrorResponseDto, FrontendErrorLogDto
from utils.telegram import send_error_to_telegram

router = APIRouter()

@router.post("/angular")
async def log_error_from_angular(error: FrontendErrorLogDto):
    user_url = f"https://uteam.top/{error.username}"
    error_message = (
        f"<b>Ошибка в Angular-приложении:</b>\n\n"
        f"<b>Сообщение об ошибке:</b> {error.errorMessage}\n"
        f"<b>Детали:</b> {error.details}\n"
        f"<b>Пользователь:</b><a href='{error.username}'>{error.username}</a>\n"
        f"<b>Время:</b> {error.timestamp}\n"
        f"<b>URL:</b>\n<pre>{error.url}</pre>"
    )
    status, response = send_error_to_telegram(error_message, 2)
    return {"status": "Лог ошибки с фронтенда отправлен", "telegram_response": response}

@router.post("/backend")
async def log_error_from_backend(error: ErrorResponseDto):
    error_message = (
        f"<b>Ошибка на сервере:</b>\n"
        f"<b>Статус:</b> {error.httpStatus}\n"
        f"<b>Детали:</b> {error.details}\n"
        f"<b>Время:</b> {error.timestamp}\n"
    )
    status, response = send_error_to_telegram(error_message, 6)
    return {"status": "Лог ошибки с бэкенда отправлен", "telegram_response": response}
