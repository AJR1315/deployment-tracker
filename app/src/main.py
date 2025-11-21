from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Data Models
class DeploymentCreate(BaseModel):
    service_name: str
    version: str
    environment: str
    status: str
    deployed_by: str

class Deployment(BaseModel):
    id: int
    service_name: str
    version: str
    environment: str
    status: str
    deployed_by: str
    deployed_at: datetime

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="Deployment Tracker",
    description="API for tracking deployment history",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "Deployment Tracker API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/version")
def get_api_version():
    return {"version": "0.1.0", "environment": "development"}

@app.post("/deployments", response_model=Deployment)
def create_deployment(deployment: DeploymentCreate, db: Session = Depends(get_db)):
    db_deployment = models.DeploymentDB(
        service_name=deployment.service_name,
        version=deployment.version,
        environment=deployment.environment,
        status=deployment.status,
        deployed_by=deployment.deployed_by,
        deployed_at=datetime.now()
    )
    db.add(db_deployment)
    db.commit()
    db.refresh(db_deployment)
    return db_deployment

@app.get("/deployments", response_model=List[Deployment])
def list_deployments(db: Session = Depends(get_db)):
    deployments = db.query(models.DeploymentDB).all()
    return deployments

@app.get("/deployments/{deployment_id}")
def get_deployment(deployment_id: int, db: Session = Depends(get_db)):
    deployment = db.query(models.DeploymentDB).filter(models.DeploymentDB.id == deployment_id).first()
    if deployment is None:
        raise HTTPException(status_code=404, detail=f"Deployment with id {deployment_id} not found")
    return deployment