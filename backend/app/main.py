from fastapi import FastAPI
from .routers import public, staff

app = FastAPI(title="Fest API", version="1.0.0")
app.include_router(public.router)
app.include_router(staff.router)

@app.get("/api/v1/health")
def health(): return {"ok": True}
