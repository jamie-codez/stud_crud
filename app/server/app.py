from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Root route"],response_description="Returns greeting message")
async def read_root():
    return {"message": "Welcome to Student crud Ops"}
