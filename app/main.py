from fastapi import FastAPI
from app.user_routes import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/users")


@app.get("/", description="This is our first route", deprecated=True)
async def root():
    return "This is a test message"




