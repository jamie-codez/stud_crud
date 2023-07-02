from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "johndoe@email.com",
                "course_of_study": "Computer Science and Technology",
                "year": 2,
                "gpa": 3.0
            }
        }


class UpdateStudentModel(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "johndoe@email.com",
                "course_of_study": "Computer Science and Technology",
                "year": 2,
                "gpa": 4.0
            }
        }


def response_model(code, message,data):
    return {
        "code": 200,
        "message": message,
        "data": data
    }


def error_response_model(code, message, error):
    return {
        "code": code,
        "message": message,
        "error": error
    }
