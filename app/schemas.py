from pydantic import BaseModel
from typing import List, Optional

class UserModel(BaseModel):
    username: str
    password: str
    role: str


class QuestionModel(BaseModel):
    question: str
    type: str
    options: Optional[List[str]] = []
    correct_answer: str


class QuizModel(BaseModel):
    title: str
    questions: List[QuestionModel]

class AttemptModel(BaseModel):
    quiz_id: str
    answers: List[str]