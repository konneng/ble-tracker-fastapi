from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="BLE Tracker API",
    description="Backend per il prototipo di tracciamento oggetti BLE",
    version="1.0.0"
)

# Permettiamo l'accesso dal frontend (es. Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in produzione meglio usare domini specifici
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "BLE Tracker backend running"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}
