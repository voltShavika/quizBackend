from fastapi import APIRouter, Depends
from bson import ObjectId
from app.database import attempts, quizzes
from app.dependencies import user_only
from app.schemas import AttemptModel

router = APIRouter(prefix="/attempt", tags=["attempt"])

@router.post("/")
def submit_attempt(attempt: AttemptModel, user=Depends(user_only)):
    quiz = quizzes.find_one({"_id": ObjectId(attempt.quiz_id)})
    if not quiz:
        return {"message": "Quiz not found"}
    score = sum(
        1 for i, q in enumerate(quiz["questions"])
        if attempt.answers[i] == q["correct_answer"]
    )
    attempts.insert_one({
        "username": user["username"],
        "quiz_id": attempt.quiz_id,
        "score": score
    })

    return {
        "status": True,
        "message": "success",
        "data": f"Total Score: {score}"
    }