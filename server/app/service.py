from fastapi import FastAPI
from server.app.routes.student_routes import student

app = FastAPI()
app.include_router(student, tags=["Student Route"], prefix="/student")


@app.get("/", tags=["Root route"], response_description="Returns greeting message")
async def read_root():
    return {"message": "Welcome to Student crud Ops"}
