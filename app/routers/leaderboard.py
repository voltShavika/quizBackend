from fastapi import APIRouter, Depends
from app.database import attempts
from app.dependencies import get_current_user

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

@router.get("/")
def get_leaderboard(user=Depends(get_current_user)):
    pipeline = [
        {"$group": {"_id": "$username", "total_score": {"$sum": "$score"}}},
        {"$sort": {"total_score": -1}},
        {"$project": {"_id": 0, "username": "$_id", "total_score": 1}}
    ]
    data = list(attempts.aggregate(pipeline))
    return {
        "status": True,
        "message": "Leaderboard fetched successfully",
        "data": data
    }
