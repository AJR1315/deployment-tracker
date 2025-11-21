from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

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

app = FastAPI(
    title="Deployment Tracker",
    description="API for tracking deployment history",
    version="0.1.0"
)

# In-memory storage (temporary - we'll replace with database later)
deployments: List[Deployment] = []
deployment_id_counter = 1

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
def create_deployment(deployment: DeploymentCreate):
    global deployment_id_counter

    new_deployment = Deployment(
        id=deployment_id_counter,
        service_name=deployment.service_name,
        version=deployment.version,
        environment=deployment.environment,
        status=deployment.status,
        deployed_by=deployment.deployed_by,
        deployed_at=datetime.now()
    )

    deployments.append(new_deployment)
    deployment_id_counter += 1

    return new_deployment

@app.get("/deployments", response_model=List[Deployment])
def list_deployments():
    return deployments

@app.get("/deployments/{deployment_id}")
def get_deployment(deployment_id: int):
    for deployment in deployments:
        if deployment.id == deployment_id:
            return deployment
    raise HTTPException(status_code=404, detail=f"Deployment with id {deployment_id} not found")