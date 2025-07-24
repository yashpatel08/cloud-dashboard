
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app.database import engine
from app.routes import resources 
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Cloud Optimization Dashboard",
    description="Backend for showing cloud resources and optimization recommendations",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return JSONResponse(content={"message": "Cloud Dashboard API is running 🚀"})

app.include_router(resources.router)
