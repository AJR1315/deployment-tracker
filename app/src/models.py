from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class DeploymentDB(Base):
    __tablename__ = "deployments"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, index=True)
    version = Column(String)
    environment = Column(String, index=True)
    status = Column(String)
    deployed_by = Column(String)
    deployed_at = Column (DateTime, default=datetime.now)