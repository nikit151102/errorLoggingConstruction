from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import error_logs, notifications

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vm-c86b4df8.na4u.ru", "http://localhost:4200", "https://rebuildpro.ru", "https://dev.rebuildpro.ru"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(error_logs.router, prefix="/log-error",  tags=["Error Logs"] )
app.include_router(notifications.router, prefix="/notify", tags=["Notifications"])
