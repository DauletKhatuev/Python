# app/schemas/question.py
from pydantic import BaseModel
class CategoryBase(BaseModel):
    name: str

class  CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryCreate):
    id: int

    class Config:
        orm_mode  = True
    
# --- QUESTION SCHEMAS ---

class QuestionBase(BaseModel):
    title: str
    body: str

class QuestionCreate(QuestionBase):
    category_id: int

class QuestionResponse(QuestionBase):
    id: int
    category: CategoryResponse

    class Config:
        orm_mode = True


