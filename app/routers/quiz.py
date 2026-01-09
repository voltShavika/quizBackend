from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from bson.errors import InvalidId

from app.dependencies import admin_only, get_current_user
from app.schemas import QuizModel
from app.database import quizzes


router = APIRouter(prefix="/quiz", tags=["quiz"])

@router.post("/")
def create_quiz(quiz: QuizModel, user=Depends(admin_only)):
    quizzes.insert_one(quiz.dict())
    return {
        "status": True,
        "message": "Quiz detail fetched successfully"
    }

@router.get("/{quiz_id}")
def get_quiz(quiz_id: str, user=Depends(get_current_user)):
    try:
        object_id = ObjectId(quiz_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid quiz ID format")
    
    data = quizzes.find_one({"_id": object_id})
    if not data:
        raise HTTPException(status_code=404, detail="Quiz not found")
    
    data["_id"] = str(data["_id"])
    return {
        "status": True,
        "message": "Quiz fetched successfully",
        "data": data
    }


@router.get("/")
def list_quizzes(user=Depends(get_current_user)):
    data = list(quizzes.find())
    for q in data:
        q["_id"] = str(q["_id"])
    return {
        "status": True,
        "message": "Quizzes fetched successfully",
        "data": data
    }