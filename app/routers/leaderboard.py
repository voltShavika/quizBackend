from fastapi import APIRouter, Depends
from app.database import attempts
from app.dependencies import get_current_user

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

@router.get("/")
def get_leaderboard(user=Depends(get_current_user)):
    data = attempts.aggregate([
        {"$group": {"_id": "$username", "total": {"$sum": "$score"}}},
        {"$sort": {"total": -1}}
    ])
    return {"data": data}