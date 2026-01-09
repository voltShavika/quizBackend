from fastapi import FastAPI
from app.routers import auth, quiz, attempt, leaderboard

app = FastAPI(title="Quiz System")

app.include_router(auth.router)
app.include_router(quiz.router)
app.include_router(attempt.router)
app.include_router(leaderboard.router)