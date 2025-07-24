
from fastapi import FastAPI
from routers import users, tags

app = FastAPI()

app.include_router(users.router, prefix="/users")
app.include_router(tags.router, prefix="/tags")

@app.get("/")
def root():
    return {"status": "BLE Tracker backend running"}
