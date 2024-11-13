from fastapi import APIRouter
from schemas.notifications import NewUserNotificationDto, NewJobNotificationDto, NewResumeNotificationDto
from utils.telegram import send_error_to_telegram

router = APIRouter()

@router.post("/new-user")
async def notify_new_user(user: NewUserNotificationDto):
    user_url = f"https://uteam.top/{user.username}"
    message = (
        f"<b>Новый пользователь:</b> <a href='{user_url}'>{user.username}</a>"
    )
    status, response = send_error_to_telegram(message, 8)
    return {"status": "Уведомление о новом пользователе отправлено", "telegram_response": response}

@router.post("/new-job")
async def notify_new_job(job: NewJobNotificationDto):
    job_url = f"https://uteam.top/vacancy/{job.id}"
    message = f"<b>Новая вакансия:</b> <a href='{job_url}'>{job.title}</a>."
    status, response = send_error_to_telegram(message, 8)
    return {"status": "Уведомление о новой вакансии отправлено", "telegram_response": response}

@router.post("/new-resume")
async def notify_new_resume(resume: NewResumeNotificationDto):
    resume_url = f"https://uteam.top/resume/{resume.id}"
    message = (
        f"<b>Новое резюме:</b> <a href='{resume_url}'>{resume.username}</a> ."
    )
    status, response = send_error_to_telegram(message, 8)
    return {"status": "Уведомление о новом резюме отправлено", "telegram_response": response}
