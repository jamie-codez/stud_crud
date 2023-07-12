from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.app.database import (add_student, retrieve_students, retrieve_student, update_student, delete_student)
from server.app.models.student import (StudentSchema, UpdateStudentModel, response_model, error_response_model)

student = APIRouter()


@student.post("/", response_description="Adds students data to the database")
async def add_student_data(student_req: StudentSchema) -> dict:
    student_body = jsonable_encoder(student_req)
    new_student = await add_student(student_body)
    return response_model(201, "Student added successfully", new_student)


@student.get("/", response_description="Gets all students from the database")
async def get_students() -> dict:
    students = await retrieve_students()
    if students:
        return response_model(200, "Students data retrieved successfully", students)
    return response_model(404, "No students found", students)


@student.get("/{doc_id}", response_description="Retrieves students data from the database")
async def get_student(doc_id: str) -> dict:
    student_doc = await retrieve_student(doc_id)
    if student_doc:
        return response_model(200, "Student retrieved successfully", student_doc)
    return error_response_model(404, "Student not found", "Unexpected error occurred")


@student.put("/{doc_id}", response_description="Updates the details of the document id parsed")
async def update_student_data(doc_id: str, update: UpdateStudentModel = Body(...)) -> dict:
    req = {k: v for k, v in update.dict().items() if v is not None}
    updated_student = await update_student(doc_id, req)
    if updated_student:
        return response_model(200, "Student updated successfully",
                              "Student with id: {} updated successfully".format(doc_id))
    return error_response_model(500, "Error occurred updating student with id: {}".format(doc_id),
                                "Unexpected error occurred")


@student.delete("/{doc_id}", response_description="Deletes the document with the parsed id")
async def delete_student_data(doc_id: str) -> dict:
    deleted_student = await delete_student(doc_id)
    if deleted_student:
        return response_model(200, "Student with id :{} deleted successfully".format(doc_id),
                              "Data deleted successfully")
    return error_response_model(500, "Error deleting student with id: {}".format(doc_id), "Error deleting")
