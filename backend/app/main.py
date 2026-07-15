from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {
        "message" : "Welcome to FlowForge"
    }

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }

@app.get("/about")
def about():
    return{
        "project" : "FlowForge",
        "version" : "1.0"
    }

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: User):
    return{
        "message" : "Coming soon!",
        "user": user
    }

@app.post("/login")
def login(user: User):
    return {
        "message" : "coming soon!"
    }