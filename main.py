from fastapi import FastAPI


app = FastAPI()

@app.get("/", description="This is our first route", deprecated=True)
async def root():
    return "This is a test message"