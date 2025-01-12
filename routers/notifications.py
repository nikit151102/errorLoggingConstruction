from fastapi import APIRouter
from schemas.notifications import UserActionDto
from utils.telegram import send_error_to_telegram
from datetime import datetime

router = APIRouter()

@router.post("/userActionInfo")
async def log_user_action_to_telegram(user_action: UserActionDto):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    user_message = (
        f"<b>Информация о пользователе:</b>\n"
        f"<b>ID пользователя:</b> {user_action.user_id}\n"
        f"<b>ФИО:</b> {user_action.user_full_name}\n"
        f"<b>Действие:</b> {user_action.action}\n"
        f"<b>Время:</b> {current_time}\n"
    )

    status, response = send_error_to_telegram(user_message, 1261) 
    return {"status": "Информация о пользователе отправлена", "telegram_response": response}