from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, quiz, attempt, leaderboard

app = FastAPI(title="Quiz System")

origins = [
    "*"
]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router)
app.include_router(quiz.router)
app.include_router(attempt.router)
app.include_router(leaderboard.router)
