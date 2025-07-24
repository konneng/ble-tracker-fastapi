
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users, tags

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users")
app.include_router(tags.router, prefix="/tags")

@app.get("/")
def read_root():
    return {"status": "BLE Tracker backend running"}
