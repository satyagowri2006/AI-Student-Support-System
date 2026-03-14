from fastapi import FastAPI

from routes.chatbot_routes import router as chatbot_router
from routes.auth_routes import router as auth_router
from routes.admission_routes import router as admission_router
from routes.academic_routes import router as academic_router
from routes.finance_routes import router as finance_router
from routes.campus_routes import router as campus_router
from routes.counseling_routes import router as counseling_router

app = FastAPI()

app.include_router(chatbot_router)
app.include_router(auth_router)
app.include_router(admission_router)
app.include_router(academic_router)
app.include_router(finance_router)
app.include_router(campus_router)
app.include_router(counseling_router)