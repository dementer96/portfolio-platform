from fastapi import FastAPI

from app.routers import auth, users

app = FastAPI(title="SecureOps Intelligence Platform")

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/health")
def health():
    return {"status": "ok"}
