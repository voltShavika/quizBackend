from fastapi import APIRouter, Depends
from app.database import users
from app.dependencies import get_current_user
from app.schemas import UserModel
from app.auth import hash_password, verify_password, create_token


router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(user: UserModel):
    if users.find_one({"username": user.username}):
        return {"message": "Username already exists"}
    users.insert_one({
        "username": user.username,
        "password": hash_password(user.password),
        "role": user.role,
    })
    return {"message": "Signup successful"}

@router.post("/login")
def login(user: UserModel):
    db_user = users.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        return {"message": "Invalid credentials"}

    token = create_token({
        "username": db_user["username"],
        "role": db_user["role"],
    })
    return {"message": "Login successful", "token": token}

@router.post("/logout")
def logout(user=Depends(get_current_user)):
    return {"message": "Logout page"}