from fastapi import APIRouter, Depends

from app.dependencies import admin_only, get_current_user
from app.schemas import QuizModel
from app.database import quizzes


router = APIRouter(prefix="/quiz", tags=["quiz"])

@router.post("/")
def create_quiz(quiz: QuizModel, user=Depends(admin_only)):
    quizzes.insert_one(quiz.dict())
    return {"message": "Quiz created successfully"}


@router.get("/")
def list_quizzes(user=Depends(get_current_user)):
    data = list(quizzes.find())
    for q in data:
        q["_id"] = str(q["_id"])
    return {"data"}