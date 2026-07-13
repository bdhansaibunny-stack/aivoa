from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import interactions, hcps, agent
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-First CRM HCP Module",
    description="Healthcare Professional interaction management system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interactions.router)
app.include_router(hcps.router)
app.include_router(agent.router)

@app.get("/")
async def root():
    return {"name": "AI-First CRM HCP Module", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.api_host, port=settings.api_port, reload=settings.debug)
