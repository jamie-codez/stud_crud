from typing import Optional
from pydantic.fields import Field as Fiel
from pydantic import BaseModel, EmailStr


class StudentSchema(BaseModel):
    username: str = Fiel(...)
    email: EmailStr = Fiel(...)
    course_of_study: str = Fiel(...)
    year: int = Fiel(..., gt=0, lt=9)
    gpa: float = Fiel(..., le=4.0)

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
