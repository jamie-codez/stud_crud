import os

import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_CON_STRING"])
database = client.students
students_collection = database.get_collection("students")


# Helpers

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "username": student["username"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"]
    }


# Add new student to the database
async def add_student(student_data: dict) -> dict:
    student = await students_collection.insert_one(student_data)
    new_student = await students_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve student
async def retrieve_student(doc_id: str) -> dict:
    student = students_collection.find_one({"_id", ObjectId(doc_id)})
    if student:
        return student_helper(student)
    return {"message": "Error retrieving students"}


# Retrieve all students
async def retrieve_students():
    students = []
    async for student in students_collection.find():
        students.append(student)
    return students


# Update Student
async def update_student(doc_id: str, data: dict) -> bool:
    # Return false if request body is empty
    if len(data) < 1:
        return False
    student = await students_collection.find_one({"_id": ObjectId(doc_id)})
    if student:
        updated_student = await students_collection.update_one({"_id": ObjectId(doc_id)}, {"$set": data})
        if updated_student:
            return True
        return False


# Delete student form database
async def delete_student(doc_id: str) -> bool:
    student = students_collection.find_one({"_id": ObjectId(doc_id)})
    if student:
        await students_collection.delete_one({"_id": ObjectId(doc_id)})
        return True
    return False
