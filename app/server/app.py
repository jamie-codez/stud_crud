from fastapi import FastAPI
from app.server.routes.students import students as StudentsRouter

app = FastAPI()
app.include_router(StudentsRouter,tags=["Students"],prefix="/student")


@app.get("/", tags=["Root route"], response_description="Returns greeting message")
async def read_root():
    return {"message": "Welcome to Student crud Ops"}
