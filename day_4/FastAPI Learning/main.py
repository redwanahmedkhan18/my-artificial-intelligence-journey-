from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI API Fundamentals"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/search")
def search(keyword: str, page: int = 1):
    return {"keyword": keyword, "page": page}


@app.post("/users")
def create_user(user: dict):
    return {
        "status": "User created",
        "user": user
    }

