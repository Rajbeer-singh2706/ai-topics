

# INstall: pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

# run: uvicorn main:app --reload
## Swagger api to test compelelty
# Docs at: http://127.0.0.1:8000/docs